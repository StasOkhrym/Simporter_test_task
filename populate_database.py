import pandas as pd
from flask import current_app
from sqlalchemy import create_engine

from app import app


def write_csv_to_db(csv_file_path: str, db_conn_str: str, db_table: str) -> None:
    engine = create_engine(db_conn_str)

    df = pd.read_csv(csv_file_path, delimiter=";", header=0)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s").dt.date
    df = df.rename(columns={" asin": "asin"})

    df.to_sql(db_table, engine, if_exists="replace", index=False)


if __name__ == "__main__":
    with app.app_context():
        write_csv_to_db(
            csv_file_path=current_app.config["CSV_FILE_PATH"],
            db_conn_str=current_app.config["CONNECTION_STRING"],
            db_table=current_app.config["TABLE_NAME"],
    )
