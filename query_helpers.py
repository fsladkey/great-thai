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


def all_cuisines():
    result = fetch_all("""
    SELECT DISTINCT
      cuisine_description
    FROM
      restaurants
    """, return_type=list)
    return sum(result, [])


def top_ten_by_grade(cuisine):
    return fetch_all("""
    SELECT
      *
    FROM
      restaurants
    WHERE
      cuisine_description = %(cuisine)s AND grade IN ('A', 'B')
    ORDER BY
      grade, score
    LIMIT
      10
    """, vals={"cuisine": cuisine})


def grade_distribution(cuisine):
    return fetch_all("""
    SELECT
      grade, COUNT(id) as num_restaurants
    FROM
      restaurants
    WHERE
      cuisine_description = %(cuisine)s AND grade IS NOT null
    GROUP BY
      grade
    """, vals={"cuisine": cuisine})
