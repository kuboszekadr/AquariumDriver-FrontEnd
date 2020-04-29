import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import get_date, data_collector
    from model import db

    app.register_blueprint(get_date.bp)
    app.register_blueprint(data_collector.bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/smart_home'
     
    db.init_app(app)

    return app


