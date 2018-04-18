from flask import Flask,url_for
from sample import sample as sample_blueprint
from exts import db
from log import log as log_blueprint
from models import User_info
from flask.ext.login import LoginManager,login_user, logout_user,login_required



import config

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.config.from_object(config)

app.register_blueprint(sample_blueprint)
app.register_blueprint(log_blueprint)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "log.render_login"


@login_manager.user_loader
def load_user(user_id):
    return User_info.query.get(user_id)



if __name__ == '__main__':
    app.run()
