from flask import Blueprint


oprecord=Blueprint('oprecord',__name__,template_folder='oprecord_temp',static_folder='static',static_url_path='/oprecord/static')

from oprecord import views