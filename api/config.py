import os

# Flask-Restplus settings
# RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
# RESTPLUS_VALIDATE = True
# RESTPLUS_MASK_SWAGGER = False
# RESTPLUS_ERROR_404_HELP = False

# SQLALCHEMY settings
SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_env_variable(name):
    """
    Get Environment Variables
    """
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# Frontend Email Urls
# FRONTEND_BASE_URL = get_env_variable('FRONTEND_BASE_URL')
# FRONTEND_VERIFY_URL = f'{FRONTEND_BASE_URL}/auth/verify'
# FRONTEND_ADMIN_INVITE_URL = f'{FRONTEND_BASE_URL}/auth/admin/invite'
# FRONTEND_PASSWORD_RECORVERY_URL = f'{FRONTEND_BASE_URL}/auth/password-recovery'


# Get db url from vars
def get_db_url(
        DB_USER=get_env_variable('DB_USERNAME'),
        DB_PASSWORD=get_env_variable('DB_PASSWORD'),
        DB_HOST=get_env_variable('DB_HOST'),
        DB_PORT=get_env_variable('DB_PORT'),
        DB_NAME=get_env_variable('DB_NAME')):
    return f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class Config:
    """
    Default configuration
    """
    DEBUG = False
    TESTING = False
    # SECRET_KEY = get_env_variable('SECRET_KEY')
    # SECURITY_PASSWORD_SALT = get_env_variable('SECURITY_PASSWORD_SALT')
    # MAIL_DEFAULT_SENDER = get_env_variable('MAIL_DEFAULT_SENDER')

    # mail settings
    # MAIL_SERVER = 'smtp.zoho.com'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True

    # email authentication
    # MAIL_USERNAME = get_env_variable('APP_MAIL_USERNAME')
    # MAIL_PASSWORD = get_env_variable('APP_MAIL_PASSWORD')

    # mail accounts
    # MAIL_DEFAULT_SENDER = get_env_variable('MAIL_DEFAULT_SENDER')

    # flask track usage include all views by default
    # TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS = 'include'


class Development(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    # JWT_SECRET_KEY = get_env_variable('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_url()


class Testing(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = True
    # JWT_SECRET_KEY = get_env_variable('JWT_SECRET_KEY')
    DB_NAME = get_env_variable('DB_NAME')
    SQLALCHEMY_DATABASE_URI = get_db_url(
        DB_NAME=get_env_variable('TEST_DB_NAME'))


class Production(Config):
    """
    Production environment configurations
    """
    SQLALCHEMY_DATABASE_URI = get_db_url()
    # JWT_SECRET_KEY = get_env_variable('JWT_SECRET_KEY')


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}


def configure_app(flask_app):
    """
    Configure App
    """

    # Load the default configuration
    # flask_app.config.from_pyfile('config.py')
    flask_app.config.from_object(app_config[get_env_variable('FLASK_ENV')])
    # flask_app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(
    #     os.path.dirname(os.path.abspath(__file__))),
    #     'files')
    # flask_app.config['ALLOWED_EXTENSIONS'] = {
    #     'pkl', 'py', 'txt', 'csv', 'xls', 'xlsx', 'doc', 'docx'}
    # flask_app.config['MAX_CONTENT_LENGTH'] = 2 * \
    #     1024 * 1024  # set max file size to 2gb

    # Setting Up App Configs
    # flask_app.config['SERVER_NAME'] = "0.0.0.0:5000"
    # flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    # flask_app.config['RESTPLUS_VALIDATE'] = RESTPLUS_VALIDATE
    # flask_app.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER
    # flask_app.config['ERROR_404_HELP'] = RESTPLUS_ERROR_404_HELP
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    return flask_app


# swagger template
# template = {
#     "swagger": "2.0",
#     "info": {
#         "title": "MamaOpe API",
#         "description": "MamaOpe Backend Service API",
#         "version": "0.0.1"
#     },
#     #   "host": "mysite.com",  # overrides localhost:500
#     #   "basePath": "/api",  # base bash for blueprint registration
#     "schemes": [
#         "http",
#         "https"
#     ]
# }
