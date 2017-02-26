from urllib.request import urlopen
import csv
import db_connection
SOURCE_URL = "https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD"

def transform_row(row):
    """Adjusts column names and value types for insertion into DB"""
    result = {}
    for col in row:
        formatted_col = col.replace(' ', '_').lower()
        col_type = db_connection.col_types[formatted_col]
        value = None if len(row[col]) == 0 else col_type(row[col])
        result[formatted_col] = value
    return result


def insert_row(restaurant, execute):
    """Inserts a restaurtant dict object into the db"""
    execute("""
        INSERT INTO restaurants ({})
        VALUES (
            %(camis)s,
            %(dba)s,
            %(boro)s,
            %(building)s,
            %(street)s,
            %(zipcode)s,
            %(phone)s,
            %(cuisine_description)s,
            %(inspection_date)s,
            %(action)s,
            %(violation_code)s,
            %(violation_description)s,
            %(critical_flag)s,
            %(score)s,
            %(grade)s,
            %(grade_date)s,
            %(record_date)s,
            %(inspection_type)s
        );""".format(db_connection.col_names), restaurant)


def populate_db(url, execute):
    csv_reader = csv.DictReader(urlopen(url, "rt"))
    for row in csv_reader:
        insert_row(transform_row(row), execute)

populate_db(SOURCE_URL, db_connection.execute)
