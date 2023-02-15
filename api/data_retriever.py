import sqlite3


def retrieve_possible_values(database, table_name):
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    # Query to retrieve earliest and latest dates
    cur.execute(
        f"SELECT MIN(timestamp) AS earliest_date, MAX(timestamp) AS latest_date "
        f"FROM {table_name}"
    )
    earliest_date, latest_date = cur.fetchone()

    # Query to retrieve distinct values of brand, stars, source, id, and asin
    cur.execute(
        f"SELECT DISTINCT brand, stars, source, id, asin "
        f"FROM {table_name} "
        f"GROUP BY brand, stars, source, id, asin "
    )
    result = cur.fetchall()
    conn.close()

    # Extract the values from the query result
    brand_names = sorted(set(row[0] for row in result))
    stars = sorted(set(row[1] for row in result))
    sources = sorted(set(row[2] for row in result))
    ids = sorted(set(row[3] for row in result))[:5]
    asins = sorted(set(row[4] for row in result))[:5]

    data = {
        "asins": asins,
        "brand_names": brand_names,
        "ids": ids,
        "stars": stars,
        "sources": sources,
        "earliest_date": earliest_date,
        "latest_date": latest_date,
    }

    return data


def retrieve_from_db(database, table_name, parameters):
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    start_date = parameters.get("startDate")
    end_date = parameters.get("endDate")
    grouping = parameters.get("Grouping")
    repr_type = parameters.get("Type")
    group_by = None

    # Construct SQL query
    columns = "timestamp, COUNT(*) AS value"

    where_clause = "timestamp BETWEEN ? AND ?"
    values = [start_date, end_date]

    # for attribute, value in parameters.get("filters").items():
    #     if attribute and value:
    #         where_clause += f" AND {attribute} = ?"
    #         values.append(value)

    if grouping == "weekly":
        group_by = "strftime('%Y-%W', timestamp)"
    elif grouping == "bi-weekly":
        group_by = (
            "strftime('%Y-', timestamp) || "
            "CASE WHEN strftime('%W', timestamp) % 2 = 0 "
            "THEN strftime('%W', timestamp) - 1 "
            "ELSE strftime('%W', timestamp) END"
        )
    elif grouping == "monthly":
        group_by = "strftime('%Y-%m', timestamp) || '-01'"

    query = (
        f"SELECT {columns} "
        f"FROM {table_name} "
        f"WHERE {where_clause} "
        f"GROUP BY {group_by} "
    )
    print(query)
    # Execute SQL query
    cur.execute(query, values)
    rows = cur.fetchall()
    conn.close()

    # Return timeline based on representation type
    if repr_type == "cumulative":
        timeline = get_cumulative_type(rows)
    else:
        timeline = get_usual_type(rows)
    print(len(timeline))
    return timeline


def get_usual_type(rows):
    return [{"date": row[0], "value": row[1]} for row in rows]


def get_cumulative_type(rows):
    def cumulative(values_list: list):
        total = 0
        for x in values_list:
            total += x
            yield total

    dates = [row[0] for row in rows]
    values = [row[1] for row in rows]
    cumulative_values = list(cumulative(values))
    return [
        {"date": date, "values": cumulative_value}
        for date, cumulative_value in zip(dates, cumulative_values)
    ]
