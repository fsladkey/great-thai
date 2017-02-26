from db_connection import fetch_all


def restaurants_where(where={}, limit=10):
    where_str = " AND ".join(["{} = %({})s".format(col, col) for col in where])
    return fetch_all("""
    SELECT
      *
    FROM
      restaurants
    WHERE
      {}
    LIMIT
      10
    """.format(where_str), where)


def all_restaurants(limit=10):
    return fetch_all("""
    SELECT
      *
    FROM
      restaurants
    LIMIT
      10
    """)
