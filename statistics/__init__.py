from flask import Blueprint


statistics=Blueprint('statistics',__name__,template_folder='statistics_temp',static_folder='static',static_url_path='/statistics/static')

from statistics import views