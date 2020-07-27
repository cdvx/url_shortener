
from flask import Response
from flask_api import status
import json

from random import choices

# from .messages import AUTH_ERRORS, ERRORS, MESSAGES
from .constants import ALPHABET


class Helpers:

    @staticmethod
    def custom_response(res, status_code, success, errors):
        """
        Custom Response Function
        """
        response = {
            'data': res,
            'errors': errors,
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
            {}, status, False,
            errors)

    @staticmethod
    def internal_server_error_response(e):
        """
        Return custom response for 500s
        """
        return Helpers.custom_response(
            {}, status.HTTP_500_INTERNAL_SERVER_ERROR, False,
            [str(e)])

    @staticmethod
    def method_not_allowed_response(e):
        """
        Return custom response for 405s
        """
        return Helpers.custom_response(
            {}, status.HTTP_405_METHOD_NOT_ALLOWED, False,
            [str(e)])

    @staticmethod
    def to_base_62(num):
        """
        Generate random short base 62 string from num
        """
        short_str = ''.join(choices(ALPHABET, k=5))
        return short_str
