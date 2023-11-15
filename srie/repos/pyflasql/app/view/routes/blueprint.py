# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Configures the address paths (URL routes)
"""
from flask import Blueprint
from ...controllers.controller import index, login, register, dashboard, logout, about
from ...controllers.srie.SQL_injection.controller import srie_SQL_injection, srie_SQL_injection_description, srie_SQL_injection_countermeasure, srie_SQL_injection_lab, srie_SQL_injection_loggedIn
from ...controllers.srie.File_upload.controller import srie_home, srie_File_upload, srie_File_upload_description,srie_File_upload_countermeasure, srie_File_upload_lab
from ...controllers.srie.Brut_Force.controller import srie_Brut_Force, srie_Brut_Force_description,srie_Brut_Force_countermeasure, srie_Brut_Force_lab, srie_Brut_Force_loggedIn
from ...controllers.user_profile.controller import user_profile
from ...controllers.toolbox.controller import toolbox_home
from ...controllers.toolbox.wtforms.controller import toolbox_wtforms_home, toolbox_wtforms_user_reg_form, toolbox_wtforms_upload_form  
from ...controllers.toolbox.database.controller import toolbox_database_home, toolbox_database_insert_data  

blueprint = Blueprint('blueprint', __name__, template_folder='../templates', static_folder='../../assets')

# Home
blueprint.route('/')(index)
blueprint.route('/login', methods=['GET', 'POST'])(login)
blueprint.route('/register', methods=['GET', 'POST'])(register)
blueprint.route('/dashboard', methods=['GET', 'POST'])(dashboard)
blueprint.route('/about', methods=['GET', 'POST'])(about)
blueprint.route('/logout', methods=['GET', 'POST'])(logout)

# User Profile
blueprint.route('/user_profile/user_profile', methods=['GET', 'POST'])(user_profile)

# SRIE
blueprint.route('/srie/home', methods=['GET', 'POST'])(srie_home)

# SQL Injection
blueprint.route('/srie/SQL_injection/home', methods=['GET', 'POST'])(srie_SQL_injection)
blueprint.route('/srie/SQL_injection/description', methods=['GET', 'POST'])(srie_SQL_injection_description)
blueprint.route('/srie/SQL_injection/countermeasure', methods=['GET', 'POST'])(srie_SQL_injection_countermeasure)
blueprint.route('/srie/SQL_injection/lab', methods=['GET', 'POST'])(srie_SQL_injection_lab)
blueprint.route('/srie/SQL_injection/loggedIn', methods=['GET', 'POST'])(srie_SQL_injection_loggedIn)


# File Upload
blueprint.route('/srie/File_upload/home', methods=['GET', 'POST'])(srie_File_upload)
blueprint.route('/srie/File_upload/description', methods=['GET', 'POST'])(srie_File_upload_description)
blueprint.route('/srie/File_upload/countermeasure', methods=['GET', 'POST'])(srie_File_upload_countermeasure)
blueprint.route('/srie/File_upload/lab', methods=['GET', 'POST'])(srie_File_upload_lab)


# Brute Force
blueprint.route('/srie/Brut_Force/home', methods=['GET', 'POST'])(srie_Brut_Force)
blueprint.route('/srie/Brut_Force/description', methods=['GET', 'POST'])(srie_Brut_Force_description)
blueprint.route('/srie/Brut_Force/countermeasure', methods=['GET', 'POST'])(srie_Brut_Force_countermeasure)
blueprint.route('/srie/Brut_Force/lab', methods=['GET', 'POST'])(srie_Brut_Force_lab)
blueprint.route('/srie/Brut_Force/loggedIn', methods=['GET', 'POST'])(srie_Brut_Force_loggedIn)

# Toolbox
blueprint.route('/toolbox/home', methods=['GET', 'POST'])(toolbox_home)
blueprint.route('/toolbox/wtforms/home', methods=['GET', 'POST'])(toolbox_wtforms_home)
blueprint.route('/toolbox/wtforms/user_reg_form', methods=['GET', 'POST'])(toolbox_wtforms_user_reg_form)
blueprint.route('/toolbox/wtforms/upload_form', methods=['GET', 'POST'])(toolbox_wtforms_upload_form)
blueprint.route('/toolbox/database/home', methods=['GET', 'POST'])(toolbox_database_home)
blueprint.route('/toolbox/database/insert_data', methods=['GET', 'POST'])(toolbox_database_insert_data)