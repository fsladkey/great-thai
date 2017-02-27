from db_connection import fetch_all, execute


def add_index():
    return execute("""
    CREATE INDEX cuisine_idx ON restaurants (cuisine_description);
    """)


def drop_index():
    return execute("""
    DROP INDEX cuisine_idx;
    """)


def all_cuisines():
    """Returns all values for cuisine_description as a list"""
    result = fetch_all("""
    SELECT DISTINCT
      cuisine_description
    FROM
      restaurants
    """, return_type=list)
    return sum(result, [])


def top_ten_by_grade(cuisine):
    """Returns the ten restaurants with the best score for a cuisine"""
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
    """Returns the frequenacy of each letter grade for a cuisine"""
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
