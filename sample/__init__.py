from flask import Blueprint

sample=Blueprint('sample',__name__,template_folder='sample_temp',static_folder='static',static_url_path='/sample/static')

from sample import views