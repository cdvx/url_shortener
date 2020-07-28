import json

from flask_api import status
from .conftest import Link

class TestUrlShortener:

    def test_url_shortening_failss_invalid_url(self, client):

        response = client.post(
            path="/", data=json.dumps(dict(link='123uf')), 
            content_type='application/json')
        assert not response.json['success']
        assert response.status == '400 BAD REQUEST'
        assert response.json['error'] == "Invalid link entered, please enter proper url to be shortened."

    def test_url_shortening_fails_empty_url_string(self, client):

        response = client.post(
            path="/", data=json.dumps(dict(link='')), 
            content_type='application/json')
        assert not response.json['success']
        assert response.status == '400 BAD REQUEST'
        assert response.json['error'] == "No link entered, please enter url to be shortened."
    
    def test_url_shortening_succeeds_valid_url(self, client):

        response = client.post(
            path="/", data=json.dumps(dict(link='https://blog.miguelgrinberg.com/post/nested-queries-with-sqlalchemy-ormwffw')), 
            content_type='application/json')
        assert response.json['success']
        assert response.status == '200 OK'
        assert not response.json['error'] 

    def test_new_record_not_created_existing_url(self, client):
        long_url = 'https://blog.miguelgrinberg.com/post/nested-queries-with-sqlalchemy-ormwffw'
        link = Link.get(long_url=long_url)

        assert link
        response = client.post(
            path="/", data=json.dumps(dict(link=long_url)), 
            content_type='application/json')
        
        assert Link.count() == 1
        assert response.json['success']
        assert response.status == '200 OK'
        assert not response.json['error']