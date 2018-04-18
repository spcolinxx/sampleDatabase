from flask import Blueprint


log=Blueprint('log',__name__,template_folder='log_temp',static_folder='static',static_url_path='/log/static')

from log import views