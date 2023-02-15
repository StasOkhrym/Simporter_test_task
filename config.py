import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE_PATH = os.path.join(BASE_DIR, "data.csv")
CONNECTION_STRING = "postgresql://postgres:postgres@localhost:5432/postgres"
TABLE_NAME = "data_table"
VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")
