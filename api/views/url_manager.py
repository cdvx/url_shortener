from flask import Blueprint, g, request
from ..utils import Helpers as hf
from flask_api import status

from .decorators import validate_link_data
from ..models.url import Link

url_shortener = Blueprint('url_shortener', __name__)


@url_shortener.route('/', methods=('POST', ))
@validate_link_data
def shorten_url():
    try:
        count = g.count
    except AttributeError:
        g.count = count = 62

    short_unique_str = hf.to_base_62(count)

    data = request.get_json()

    link = data['link']

    record_exists = Link.exists(link, 'long_url') 
    if record_exists:
        short_url = Link.get(long_url=link)
        return hf.custom_response(
            dict(shortened_url=short_url.to_dict(),message='Url successfully retrieved.'),
            status.HTTP_200_OK, True, [] )


    # short_unique_str = short_unique_str[:5]
    short_url = Link(long_url=link, short_url=short_unique_str)


    success = short_url.shorten_url()
    if success:
        count += 3
        g.count = count
        return hf.custom_response(
            dict(shortened_url=short_url.to_dict(),message='Url successfully shortened.'),
            status.HTTP_200_OK, True, [] )

    return hf.custom_response(
        {}, status.HTTP_417_EXPECTATION_FAILED,
        False, ['Failed to shorten url, please try again.']
    )


@url_shortener.route('/', methods=('GET',))
def got_to():
    url = request.args.get('url', None)
    if not url:
        return hf.custom_response(dict(message="Enter url to shorten."), status.HTTP_200_OK, True, [])
    url = Link.get_short_url(url)
    if url:
        long_url = url.long_url
        return redirect(long_url)
    return hf.custom_response({}, status.HTTP_404_NOT_FOUND, False, [f'Requested url, {request.base_url}{url} not found.'])
