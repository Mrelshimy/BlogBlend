import os


class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql://{os.environ["DB_USER"]}:{os.environ["DB_PASS"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'
    SECRET_KEY = os.urandom(32)
    # SECRET_KEY = os.environ['SECRET_KEY']