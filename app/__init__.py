from flask import (
    Flask,
    render_template,
)
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'web'
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = False
db = SQLAlchemy(app)


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图 (url_prefix 区分路由)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
