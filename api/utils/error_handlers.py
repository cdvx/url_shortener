from flask_api import status

from .helpers import Helpers as hf


def error_handlers(app):
    """Set up error handlers"""

    @app.errorhandler(500)
    def internal_server_error(e):
        return hf.internal_server_error_response(e)

    @app.errorhandler(400)
    def bad_request(e):
        return hf.bad_request_response(
            status.HTTP_404_NOT_FOUND,
            [str(e)])

    @app.errorhandler(404)
    def not_found(e):
        return hf.custom_response(
            {},
            status.HTTP_404_NOT_FOUND,
            False,
            [str(e)])

    @app.errorhandler(405)
    def method_not_allowed(e):
        return hf.method_not_allowed_response(e)

    return app
