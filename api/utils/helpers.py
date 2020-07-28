
import json
from random import choices

from flask import Response
from flask_api import status

from .constants import ALPHABET


class Helpers:

    @staticmethod
    def custom_response(res, status_code, success, errors):
        """
        Custom Response Function
        """
        response = {
            'short_url': res,
            'error': errors,
            'success': success
        }
        return Response(
            mimetype="application/json",
            response=(json.dumps(response)),
            status=status_code
        )

    @staticmethod
    def bad_request_response(status, errors):
        """
        Return custom response for bad request data
        """
        return Helpers.custom_response(
            False, status, False,
            errors)

    @staticmethod
    def internal_server_error_response(e):
        """
        Return custom response for 500s
        """
        return Helpers.custom_response(
            False, status.HTTP_500_INTERNAL_SERVER_ERROR, False,
            'Something went wrong, if problem persists please contact us @cdvx on github.')

    @staticmethod
    def method_not_allowed_response(e):
        """
        Return custom response for 405s
        """
        return Helpers.custom_response(
            False, status.HTTP_405_METHOD_NOT_ALLOWED, False,
            'Mehtod not allowed')

    @staticmethod
    def to_base_62():
        """
        Generate random short string
        """
        short_str = ''.join(choices(ALPHABET, k=5))
        return short_str
