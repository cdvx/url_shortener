import re
from functools import wraps

from flask import request
from flask_api import status

from ..utils import URL_REGEX
from ..utils import Helpers as hf


def validate_link_data(func):
    """
    Validate link to be shortened
    """
    @wraps(func)
    def validated_request(*args, **kwargs):

        if request.method == 'GET':
            return func(*args, **kwargs)

        request_is_json = request.is_json
        req_data = request.get_json()
        link = req_data.get('link', '').strip()

        invalid_link_data = not request_is_json or req_data \
            == {} or not link

        if invalid_link_data:
            return hf.bad_request_response(status.HTTP_400_BAD_REQUEST,
                                           "No link entered, please enter url to be shortened.")
        valid_url = re.fullmatch(URL_REGEX, link)
        if not valid_url:
            return hf.bad_request_response(status.HTTP_400_BAD_REQUEST,
                                           "Invalid link entered, please enter proper url to be shortened.")

        return func(*args, **kwargs)
    return validated_request
