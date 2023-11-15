# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for SQL Injection
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB, UserSQLInjection
from ...utils import get_shell_output, CheckIf
from ....models.srie.SQL_injection.forms import SQLInjectionForm

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

@login_required
def srie_home():
    """
        Handles the logic for /srie/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_home')+'.html', username=username)

@login_required
def srie_SQL_injection():
    """
        Handles the logic for /srie/SQL_injection/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/SQL_injection/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_SQL_injection')+'.html', username=username)

@login_required
def srie_SQL_injection_description():
    """
        Handles the logic for view/templates/srie/SQL_injection/description.html
        Login is required to view this page

        Show the description of SQL injections.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/SQL_injection/description.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    return render_template(url_for('blueprint.srie_SQL_injection_description')+'.html')


@login_required
def srie_SQL_injection_countermeasure():
    """
        Handles the logic for view/templates/srie/SQL_injection/countermeasure.html
        Login is required to view this page

        Show the countermeasure of SQL injections.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/SQL_injection/countermeasure.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    return render_template(url_for('blueprint.srie_SQL_injection_countermeasure')+'.html')

@login_required
def srie_SQL_injection_lab():
    """
        Handles the logic for view/templates/srie/SQL_injection/lab.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/SQL_injection/lab.html with content passed as a context variable
        """
    # Create a dictionary to store entered data
    content = {"form" : SQLInjectionForm(),
                "username": "", 
                "password": ""
            }
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        username = content["form"].username.data
        password = content["form"].password.data
        content["username"] = username
        content["password"] = password

        # Create a connection to the database
        engine = create_engine('sqlite:///instance/database.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a query to the database

        
        #To find the name of the table (user_sql_injection)
        #table_names = engine.table_names()
        #for table_name in table_names:
        #   print(table_name)

  
        query = f"SELECT * FROM user_sql_injection WHERE username = '{username}' AND password = '{password}'"
      
        # Execute the query
        result = session.execute(query)
        content["query"] = query
        rows = result.fetchall()
        # Check if the query returned a result

        if len(rows) == 0:
            content["result"] = "No result"
        else:
            content["result"] = [rows[i] for i in range(len(rows))]
        
        # Close the connection to the database
        session.close()
        if len(rows)==1 and rows[0][1] == 'administrator':
            return render_template(url_for('blueprint.srie_SQL_injection_loggedIn')+'.html', content=content)

        return render_template(url_for('blueprint.srie_SQL_injection_lab')+'.html', content=content)
    return render_template(url_for('blueprint.srie_SQL_injection_lab')+'.html', content=content)

@login_required
def srie_SQL_injection_loggedIn():
    """
        Handles the logic for view/templates/srie/SQL_injection/loggedIn.html
        Login is required to view this page

        Go to loggedIn if administrator credentials is entered.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/SQL_injection/loggedIn.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    return render_template(url_for('blueprint.srie_SQL_injection_loggedIn')+'.html')