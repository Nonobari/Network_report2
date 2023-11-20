# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.

import os
from flask import Flask, render_template, url_for, redirect, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output, CheckIf, get_current_directory
from ....models.srie.File_upload.forms import FileUploadForm
from werkzeug.utils import secure_filename
from ....models.toolbox.forms import ToolboxUploadForm 
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
def srie_File_upload():
    """
        Handles the logic for /srie/File_Upload/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/File_Upload/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_File_upload')+'.html', username=username)

@login_required
def srie_File_upload_description():
    """
        Handles the logic for view/templates/srie/File_Upload/desciprtion.html
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/File_Upload/description.html with content passed as a context variable
        """
    return render_template(url_for('blueprint.srie_File_upload_description')+'.html')



@login_required
def srie_File_upload_countermeasure():
    """
        Handles the logic for view/templates/srie/File_Upload/countemeasure.html
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/File_Upload/countermeasure.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    UPLOAD_FOLDER = os.path.join(get_current_directory(), "app/assets/uploads")
    content = {"form": ToolboxUploadForm(),
               "confirm": False,
               "file_path": False,
               "file_url": False,
               "filename": False
               }

    if content["form"].validate_on_submit():
        # Form has been submitted and is valid
        # Access form data using content["form"].field_name.data
        image = content["form"].image.data
        if image:
            filename = secure_filename(image.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(file_path)
            content["file_path"] = file_path
            content["filename"] = filename
            content["file_url"] = url_for('blueprint.static', filename=f'uploads/{filename}')

            # Perform further processing on the uploaded image if needed
            content["confirm"] = True
            flash('Image uploaded successfully!', 'Success')
        
        # Redirect to success page or do other logic
        return render_template(url_for('blueprint.srie_File_upload_countermeasure')+'.html',content=content)
    return render_template(url_for('blueprint.srie_File_upload_countermeasure')+'.html', content=content)


@login_required
def srie_File_upload_lab():
    """
        Handles the logic for view/templates/srie/File_Upload/lab.html
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/File_Upload/lab.html with content passed as a context variable
        """

    UPLOAD_FOLDER = os.path.join(get_current_directory(), "app/assets/uploads")
    content = {"form": FileUploadForm(),
               "confirm": False,
               "file_path": False,
               "file_url": False,
               "filename": False
               }

    if content["form"].validate_on_submit():
        # Form has been submitted and is valid
        # Access form data using content["form"].field_name.data
        image = content["form"].image.data
        if image:
            filename = secure_filename(image.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(file_path)
            content["file_path"] = file_path
            content["filename"] = filename
            content["file_url"] = url_for('blueprint.static', filename=f'uploads/{filename}')

            # Perform further processing on the uploaded image if needed
            content["confirm"] = True
            flash('Image uploaded successfully!', 'Success')
        
        # Redirect to success page or do other logic
        return render_template(url_for('blueprint.srie_File_upload_lab')+'.html', content=content)
    return render_template(url_for('blueprint.srie_File_upload_lab')+'.html', content=content)

