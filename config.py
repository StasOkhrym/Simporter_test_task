import os

from flask import Config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(Config):
    CONNECTION_STRING = (
        "postgresql://postgres:postgres@localhost:5432/postgres"
    )
    CSV_FILE_PATH = os.path.join(BASE_DIR, "data.csv")
    VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TABLE_NAME = "dev_data_table"
    print("THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.")


class ProductionConfig(BaseConfig):
    DEBUG = False
    TABLE_NAME = "data_table"
