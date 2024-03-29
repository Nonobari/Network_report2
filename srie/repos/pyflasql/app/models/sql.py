# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Communicates with the SQLite database
"""
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
# Initializes a database object that enables interaction with the database using SQLAlchemy's functionalities.
db = SQLAlchemy()


class UserDB(db.Model, UserMixin):
    """
    Represents a User model in the database.
    
    Attributes:
        - id: Integer field, primary key of the User.
        - username: String field, username of the User, must be unique and not nullable.
        - password: String field, password of the User, not nullable.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Integer, nullable=False, unique=False)

class UserSQLInjection(db.Model):
    """
    Represents a user for the SQL injection database.
    
    Attributes:
        - id: Integer field, primary key of the User.
        - username: String field, username of the User, must be unique and not nullable.
        - password: String field, password of the User, not nullable.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class UserBrutForce(db.Model):
    """
    Represents a user for the SQL injection database.
    
    Attributes:
        - id: Integer field, primary key of the User.
        - username: String field, username of the User, must be unique and not nullable.
        - password: String field, password of the User, not nullable.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    remainingAttempts = db.Column(db.Integer, nullable=False, unique=False)
    lastAttempt = db.Column(db.DateTime, nullable=True, unique=False)

class ToolboxBookLibraryDB(db.Model):
    """
    Represents a User model in the database.
    
    Attributes:
        - id: Integer field, primary key of the User.
        - username: String field, username of the User, must be unique and not nullable.
        - password: String field, password of the User, not nullable.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=False)
    author = db.Column(db.String(200), nullable=False, unique=False)
    description = db.Column(db.String(200), nullable=False, unique=False)
    cover = db.Column(db.String(200), nullable=False, unique=False)