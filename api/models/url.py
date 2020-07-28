
import sqlalchemy
from flask_api import status
from sqlalchemy.sql import func

from ..utils import Helpers as hf
from . import db
from .model_operations import ModelOperations


class Link(db.Model, ModelOperations):
    """
    Link Model
    """

    # table name
    __tablename__ = 'shortened_urls'

    url_id = db.Column(db.BigInteger, primary_key=True)
    long_url = db.Column(
        db.String(512), nullable=False, unique=True)
    short_url = db.Column(
        db.String(5), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False)

    @staticmethod
    def get_short_url(short_url):
        """
        Get a specific short url for by given long_url
        """
        return Link.get(short_url=short_url)

    def __repr__(self):
        return f'Link: <long_url {self.long_url} -- short_url {self.short_url}>'


    def shorten_url(self):
        """
        Create Link
        """
        try:
            self.save()
            return True

        except Exception as e:
            print("Error saving to db: ", e)
            return False
