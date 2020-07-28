
from ..utils import EXISTS
from . import db


class ModelOperations:
    """Mixin class with generic model operations."""

    def save(self):
        """
        Save a model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def count(cls):
        """
        Returns total entries in the database
        """
        return cls.query.count()


    @classmethod
    def get(cls, **kwargs):
        """
        return entries by key
        """
        return cls.query.filter_by(**kwargs).one_or_none()

    
    @classmethod
    def exists(cls, value, column='id'):
        """Verifies whether a record for the specified column and value exists in the database
        Returns:
            bool: True if the value exists, False otherwise
        """
        query = EXISTS.format(
            table=cls.__table__.name, column=column, value=value)
        result = db.engine.execute(query).scalar()
        if result:
            return True
        return False
