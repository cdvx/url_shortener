from flask import Flask, render_template
from os import path
from .config import configure_app
from .utils import error_handlers
from .views import url_shortener 
from .models.url import Link
from .models import db
from flask_migrate import Migrate

from flask_cors import CORS

dir_path = path.dirname(path.realpath(__file__))


def create_app():
    """
    Create app
    """
    app = Flask(__name__, root_path=dir_path)

    CORS(app)

    # Configure app
    app = configure_app(app)

    # setup error handling
    app = error_handlers(app)

    # Register blueprint for url_shortener
    app.register_blueprint(url_shortener)

    # Database setup
    db.init_app(app)

    # initialize migration scripts
    migrate = Migrate(app, db)


    with app.app_context():
        db.create_all()


    # State Routes
    @app.route('/yow')
    def api_documentation():
        return render_template("main.html")

    return app
