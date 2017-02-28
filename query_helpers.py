from db_connection import fetch_all, execute


def add_indices():
    "Adds indices to table on commonly searched columns"
    return execute("""
    CREATE INDEX cuisine_idx ON restaurants (cuisine_description);
    CREATE INDEX grade_idx ON restaurants (grade);
    CREATE INDEX score_idx ON restaurants (score);
    """)


def drop_indices():
    "Drops all indices on the restaurants table"
    return execute("""
    DROP INDEX cuisine_idx;
    DROP INDEX grade_idx;
    DROP INDEX score_idx;
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
    """
    Returns the ten restaurants with the best score for a cuisine.
    Restaurants are ordered by grade and score and preference is given to
    those with a non-critical violation.
    """
    return fetch_all("""
    SELECT
      *
    FROM
      restaurants
    WHERE
      cuisine_description = %(cuisine)s AND grade IN ('A', 'B')
    ORDER BY
      grade, score, critical_flag DESC
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
