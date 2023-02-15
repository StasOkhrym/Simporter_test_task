import pandas as pd
from sqlalchemy import create_engine

import config


def write_csv_to_db(csv_file_path, db_conn_str, db_table):
    engine = create_engine(db_conn_str)

    df = pd.read_csv(csv_file_path, delimiter=";", header=0)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s").dt.date
    df = df.rename(columns={" asin": "asin"})

    df.to_sql(db_table, engine, if_exists="replace", index=False)


if __name__ == "__main__":
    write_csv_to_db(
        csv_file_path=config.CSV_FILE_PATH,
        db_conn_str=config.CONNECTION_STRING,
        db_table=config.TABLE_NAME,
    )
