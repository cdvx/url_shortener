
from marshmallow import INCLUDE, Schema, fields, ValidationError

# from ...utils.messages import AUTH_ERRORS as AUTH_MESSAGES, MESSAGES, ERRORS
from . import db
from flask_api import status
# from ...utils.validators import Validators as vd
from sqlalchemy.sql import func
from ..utils import Helpers as hf
from .model_operations import ModelOperations
import sqlalchemy


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

    def to_dict(self):
        """
        Return Link Dictionary
        """
        schema = ShortenedUrlSchema()
        return schema.dump({
            'url_id': self.url_id,
            'long_url': self.long_url,
            'short_url': self.short_url,
            'created_at': self.created_at,
        })

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

        

    def delete_url(self):
        """
        Delete Link record
        """
        self.delete()


class ShortenedUrlSchema(Schema):
    """
    Link Schema
    """
    url_id = fields.Int(dump_only=True)
    long_url = fields.URL()
    short_url = fields.URL()

    class Meta:
        unknown = INCLUDE
        ordered = True
        datetimeformat = '%d/%m/%Y'
        additional = ('created_at', )
