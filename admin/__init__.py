from flask import Blueprint

admin_blue = Blueprint('admin', __name__)

from admin import viewmodel