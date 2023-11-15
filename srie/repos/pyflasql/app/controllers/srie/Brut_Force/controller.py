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
# from flask_migrate import Migrate
from ....models.sql import db, UserDB, UserBrutForce, UserSQLInjection
from ...utils import get_shell_output
from ....models.srie.Brut_Force.forms import LoginForm


from ....models.app import PyFlaSQL



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
        Handles the logic for view/templates/srie/tp2_scanning_networds/pingaddr.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/Brut_Force/description.html with content passed as a context variable
        """
 
    return render_template(url_for('blueprint.srie_Brut_Force_description')+'.html')


@login_required
def srie_Brut_Force_countermeasure():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/whois.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/whois.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    
    return render_template(url_for('blueprint.srie_File_upload_countermeasure')+'.html')


@login_required
def srie_Brut_Force_lab():
    """
    Handles the logic for /login page

    Args:
        - None.

    Returns:
        - rendered .html template (dashboard.html if login success or login.html if login fail)
    """
    content = LoginForm()
    if content.validate_on_submit():
        lignes = UserSQLInjection.query.all()
        #lignes = UserBrutForce.query.all()
        for l in lignes:
            print(f"{l.username} {l.password}")
        user = UserBrutForce.query.filter_by(username=content.username.data).first()
        if user:
            print("oui")
            if (user.password == content.password.data):
                print(user.password)
                print(content.password.data)
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