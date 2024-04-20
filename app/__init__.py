import os
from flask import Flask,redirect,render_template
from . import auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
    )
    
    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(auth.bp)

    return app