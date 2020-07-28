import os

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


class Development(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_url()


class Testing(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = True
    DB_NAME = get_env_variable('DB_NAME')
    SQLALCHEMY_DATABASE_URI = get_db_url(
        DB_NAME=get_env_variable('TEST_DB_NAME'))


class Production(Config):
    """
    Production environment configurations
    """
    SQLALCHEMY_DATABASE_URI = get_db_url()


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}


def configure_app(flask_app):
    """
    Configure App
    """
    flask_app.config.from_object(app_config[get_env_variable('FLASK_ENV')])
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    return flask_app

