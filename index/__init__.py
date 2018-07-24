from flask import Blueprint


index=Blueprint('index',__name__,template_folder='index_temp',static_folder='static',static_url_path='/index/static')

from index import views