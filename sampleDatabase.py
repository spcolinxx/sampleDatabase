from flask import Flask,url_for
from sample import sample as sample_blueprint
from exts import ormdb
from log import log as log_blueprint
from statistics import statistics as statistics_blueprint
from oprecord import oprecord as oprecord_blueprint
from index import index as index_blueprint
from models import User_obj
from flask.ext.login import LoginManager,login_user, logout_user,login_required
from log import mongo
import exts



import config

app = Flask(__name__)
ormdb.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.config.from_object(config)

app.register_blueprint(sample_blueprint)
app.register_blueprint(log_blueprint)
app.register_blueprint(statistics_blueprint)
app.register_blueprint(oprecord_blueprint)
app.register_blueprint(index_blueprint)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "log.render_login"


@login_manager.user_loader
def load_user(user_id):
    # return User_info.query.get(user_id)
    cnn=exts.create_mongo_cnn()
    user=mongo.search_user({'user_account':user_id},cnn)
    cnn.close()

    return User_obj(user['user_account'],user['user_psd'],user['user_lv'])



if __name__ == '__main__':
    app.run()
