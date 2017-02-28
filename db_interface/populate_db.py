from urllib2 import urlopen
import csv
import db_connection
from query_helpers import drop_indices, add_indices
SOURCE_URL = "https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD"
# SOURCE_URL = "http://localhost:8000/data.csv"


def transform_row(row):
    """Adjusts column names and value types for insertion into DB"""
    result = {}
    for col in row:
        formatted_col = col.replace(' ', '_').lower()
        col_type = db_connection.col_types[formatted_col]
        value = None if len(row[col]) == 0 else col_type(row[col])
        result[formatted_col] = value
    return result


def insert_inspection():
    """Inserts a restaurtant dict object into the db"""
    return ("""
        INSERT INTO inspections ({})
        VALUES (
            %(camis)s,
            %(action)s,
            %(critical_flag)s,
            %(grade)s,
            %(grade_date)s,
            %(inspection_date)s,
            %(inspection_type)s,
            %(record_date)s,
            %(score)s,
            %(violation_code)s,
            %(violation_description)s
        );""".format(", ".join(db_connection.inspection_col_names)))


def insert_restaurant():
    """Inserts a restaurtant dict object into the db"""
    return ("""
        INSERT INTO restaurants ({})
        VALUES (
            %(camis)s,
            %(dba)s,
            %(boro)s,
            %(building)s,
            %(street)s,
            %(zipcode)s,
            %(phone)s,
            %(cuisine_description)s
        );""".format(", ".join(db_connection.restaurtant_col_names)))


def populate_db(url):
    """Reads csv file from a url and inserts each line into the db"""
    restaurant_ids = set([])
    drop_indices()
    count = 0
    try:
        with db_connection.connect() as connection:
            with connection.cursor() as cur:
                csv_reader = csv.DictReader(urlopen(url))
                for row in csv_reader:
                    restaurant_id = row["CAMIS"]
                    transformed = transform_row(row)
                    if restaurant_id in restaurant_ids:
                        cur.execute(insert_inspection(), transformed)
                    else:
                        cur.execute(insert_restaurant(), transformed)
                        cur.execute(insert_inspection(), transformed)
                        restaurant_ids.add(restaurant_id)
                    count += 1
                    print(count)
    finally:
        add_indices()

populate_db(SOURCE_URL)
