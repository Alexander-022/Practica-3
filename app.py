from flask import Flask
import logging
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import config.config
from flask_cors import CORS
from flask import Flask, request, jsonify, make_response
from werkzeug.utils import secure_filename
import os

db = SQLAlchemy()

logging.basicConfig(level=logging.DEBUG)


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    
    

    
    CORS(app)
    #todo
    app.config.from_object('config.config.config')
    db.init_app(app)
    with app.app_context():
        from routes.api import api
        from routes.api_persona import api_persona
        from routes.api_producto import api_producto
        from routes.api_loteproducto import api_loteproducto
        #from routes.api_censu import api_censu
        app.register_blueprint(api)
        app.register_blueprint(api_persona)
        app.register_blueprint(api_producto)
        app.register_blueprint(api_loteproducto)
        #app.register_blueprint(api_censu)
        #create table bd
        db.create_all()
        #db.drop_all()
    return app