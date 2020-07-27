from flask_sqlalchemy import SQLAlchemy


# Initialise DB
try:
    db = SQLAlchemy()

    def reset_database():
        db.drop_all()
        db.create_all()

except Exception as e:
    print("error occured whilw connecting to db -", e)