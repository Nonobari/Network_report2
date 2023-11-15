# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange


class LoginForm(FlaskForm):
    """
    Represents a login form for user authentication.

    Attributes:
        - username: StringField with validators for input required and length constraints,
        and a placeholder for username input.
        - password: PasswordField with validators for input required and length constraints,
        and a placeholder for password input.
        - submit: SubmitField with label 'Login' for submitting the form.
    """
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "    "})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField('Login')