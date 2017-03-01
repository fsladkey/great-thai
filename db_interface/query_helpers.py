from db_connection import fetch, execute


def add_indices():
    "Adds indices to table on commonly searched columns"
    return execute("""
    CREATE INDEX camis_idx ON restaurants (camis);
    CREATE INDEX cuisine_idx ON restaurants (cuisine_description);
    CREATE INDEX restaurant_idx ON inspections (restaurant_camis);
    CREATE INDEX grade_idx ON inspections (grade);
    CREATE INDEX score_idx ON inspections (score);
    CREATE INDEX date_idx ON inspections (record_date);
    """)


def drop_indices():
    "Drops all indices on the restaurants table"
    return execute("""
    DROP INDEX camis_idx;
    DROP INDEX cuisine_idx;
    DROP INDEX restaurant_idx;
    DROP INDEX grade_idx;
    DROP INDEX score_idx;
    DROP INDEX date_idx;
    """)


def all_cuisines():
    """Returns all values for cuisine_description as a list"""
    result = fetch("""
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
    return fetch("""
    SELECT
      restaurants.*,
      MIN(inspections.grade) AS max_grade,
      SUM(inspections.score) AS total_score
    FROM
      restaurants
    JOIN
      inspections ON restaurants.camis = inspections.restaurant_camis
    LEFT OUTER JOIN
      inspections as latest ON (latest.restaurant_camis = inspections.restaurant_camis AND
      inspections.record_date < latest.record_date)
    WHERE
      cuisine_description = %(cuisine)s AND
      inspections.grade <= 'B' AND
      latest.record_date IS NULL
    GROUP BY
      restaurants.id
    ORDER BY
      max_grade, total_score
    LIMIT
     10
    """, vals={"cuisine": cuisine})


def grade_distribution(cuisine):
    """Returns the frequenacy of each letter grade for a cuisine"""
    return fetch("""
    SELECT
      grade, COUNT(DISTINCT inspections.id) AS num_restaurants
    FROM
      restaurants
    LEFT OUTER JOIN
      inspections ON (inspections.restaurant_camis = restaurants.camis)
    WHERE
      restaurants.cuisine_description = %(cuisine)s AND grade IS NOT null
    GROUP BY
      grade
    """, vals={"cuisine": cuisine})
