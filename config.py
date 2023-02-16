import os

from flask import Config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV_FILE_PATH = os.path.join(BASE_DIR, "data.csv")
# CONNECTION_STRING = "postgresql://postgres:postgres@localhost:5432/postgres"
# TABLE_NAME = "data_table"
# VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")


class DevelopmentConfig(Config):
    DEBUG = True
    CONNECTION_STRING = "postgresql://postgres:postgres@localhost:5432/postgres"
    CSV_FILE_PATH = os.path.join(BASE_DIR, "data.csv")
    TABLE_NAME = "dev_data_table"
    VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class ProductionConfig(Config):
    DEBUG = False
    CONNECTION_STRING = "postgresql://postgres:postgres@localhost:5432/postgres"
    CSV_FILE_PATH = os.path.join(BASE_DIR, "data.csv")
    TABLE_NAME = "data_table"
    VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")