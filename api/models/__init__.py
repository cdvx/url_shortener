from flask_sqlalchemy import SQLAlchemy


# Initialise DB
try:
    db = SQLAlchemy()

    def reset_database():
        db.drop_all()
        db.create_all()

except Exception as e:
    print("Error occured while connecting to db -", e)