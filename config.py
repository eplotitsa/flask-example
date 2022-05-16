import pathlib

from sqlalchemy import true

BASE_DIR= pathlib.Path(__file__).parent

class Config:
    SQLALCHEMY_DATABASE_URI='sqlite:///' + str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #EXPLAIN_TEMPLATE_LOADING = True