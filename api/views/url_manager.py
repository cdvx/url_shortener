from flask import Blueprint, g, jsonify, redirect, render_template, request
from flask_api import status

from ..models.url import Link
from ..utils import Helpers as hf
from .decorators import validate_link_data

url_shortener = Blueprint('url_shortener', __name__)


@url_shortener.route('/', methods=('POST', 'GET' ))
@validate_link_data
def shorten_url():
    if request.method == 'GET':
        return render_template('main.html', success=True)

    short_unique_str = hf.to_base_62()
    if Link.exists(short_unique_str, "short_url"):
        short_unique_str = hf.to_base_62()

    data = request.get_json()

    link = data['link']
    record_exists = Link.exists(link, 'long_url') 
    if record_exists:
        short_url = Link.get(long_url=link).short_url
        return hf.custom_response(
            short_url,
            status.HTTP_200_OK, True, False )

    short_url = Link(long_url=link, short_url=short_unique_str)

    success = short_url.shorten_url()
    if success:
        return hf.custom_response(
            short_url.short_url,
            status.HTTP_200_OK, True, False )
    return hf.custom_response(
        False, status.HTTP_417_EXPECTATION_FAILED,
        False, 'Failed to shorten url, please try again.'
    )

@url_shortener.route('/<url>', methods=('GET',))
def get_url(url): 
    url = Link.get_short_url(url)
    long_url = url.long_url
    return redirect(long_url)
