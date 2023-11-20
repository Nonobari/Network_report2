# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP2 - Scanning Networks
"""
from flask import Flask, render_template, url_for, redirect, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sympy import sec
# from flask_migrate import Migrate
from ....models.sql import db, UserDB, UserBrutForce, UserSQLInjection
from ...utils import get_shell_output
from ....models.srie.Brut_Force.forms import LoginForm


from ....models.app import PyFlaSQL
import time
import datetime

@login_required
def srie_Brut_Force():
    """
        Logic for /srie/Brut_Force/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/Brut_Force/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_Brut_Force')+'.html', username=username)

@login_required
def srie_Brut_Force_description():
    """
        Handles the logic for view/templates/srie/Brut_Force/description.html
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/Brut_Force/description.html with content passed as a context variable
        """
 
    return render_template(url_for('blueprint.srie_Brut_Force_description')+'.html')



@login_required
def srie_Brut_Force_countermeasure():
    """
        Handles the logic for view/templates/srie/Brut_Force/countermeasure.html
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/Brut_Force/countermeasure.html with content passed as a context variable
        """
    delayTimeIfFailed = datetime.timedelta(minutes=5)


    content = LoginForm()
    def checkPassword(user):
        if (user.password == content.password.data):
            user.remainingAttempts = 3
            db.session.commit()
            return True
        else:
            user.remainingAttempts = user.remainingAttempts - 1
            db.session.commit()
            if (user.remainingAttempts == 0):
                user.lastAttempt = datetime.datetime.now()
                db.session.commit()
                flash(f'Login or password incorrect! You have no more attempts. Try again the {(user.lastAttempt + delayTimeIfFailed).strftime("%d/%m/%y at %H:%M:%S")}', 'Error')
            else :
                flash(f'Login or password incorrect! {user.remainingAttempts} attempts remaining', 'Error')
            return False


    if content.validate_on_submit():
        user = UserBrutForce.query.filter_by(username=content.username.data).first()
        #make a query to the database to check if the user exists with brut force protection
        if user:
            if (user.remainingAttempts > 0):
                 if (checkPassword(user)):
                        return render_template(url_for('blueprint.srie_Brut_Force_loggedIn')+'.html', content=content)
            else:
                if (user.lastAttempt + delayTimeIfFailed < datetime.datetime.now()):
                    user.remainingAttempts = 3
                    db.session.commit()
                    if (checkPassword(user)):
                        return render_template(url_for('blueprint.srie_Brut_Force_loggedIn')+'.html', content=content)

                else:
                    flash(f'Login or password incorrect! You have no more attempts. Try again the {(user.lastAttempt + delayTimeIfFailed).strftime("%d/%m/%y at %H:%M:%S")}', 'Error')
        else:
            flash(f'Login or password incorrect!', 'Error')
            
    return render_template(url_for('blueprint.srie_Brut_Force_countermeasure')+'.html', content = content)


@login_required
def srie_Brut_Force_lab():
    """
    Handles the logic for /login page

    Args:
        - None.

    Returns:
        - rendered .html template
    """
    content = LoginForm()
    if content.validate_on_submit():
        user = UserBrutForce.query.filter_by(username=content.username.data).first()
        if user:
            if (user.password == content.password.data):
                return render_template(url_for('blueprint.srie_Brut_Force_loggedIn')+'.html', content=content)
        flash('Login or password incorrect!', 'Error')
       
        # Redirect to success page or do other logic
    return render_template(url_for('blueprint.srie_Brut_Force_lab')+'.html', content=content)

@login_required
def srie_Brut_Force_loggedIn():
    """
        Handles the logic for view/templates/srie/Brut_Force/loggedIn.html
        Login is required to view this page

        Go to loggedIn if administrator credentials is entered.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/Brut_Force/loggedIn.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    return render_template(url_for('blueprint.srie_Brut_Force_loggedIn')+'.html')