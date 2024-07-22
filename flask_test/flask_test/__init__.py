from flask import Flask, redirect, url_for
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Configuration stuff
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Test endpoint
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # Import blueprint
    from . import modeling 
    app.register_blueprint(modeling.bp)
    
    # Redirect base URL to blueprint
    @app.route('/')
    def index():
        return redirect(url_for('modeling.modeling'))

    return app