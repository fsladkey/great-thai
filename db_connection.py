import os
import psycopg2
import psycopg2.extras
import datetime
from urlparse import urlparse


def to_date(string_formatted_date):
    """Parse data in the format of mm/dd/yyyy into datatime object"""
    return datetime.datetime.strptime(string_formatted_date, "%m/%d/%Y")

col_types = {
    "camis": int,
    "score": int,
    "dba": str,
    "boro": str,
    "building": str,
    "street": str,
    "zipcode": str,
    "phone": str,
    "cuisine_description": str,
    "inspection_date": to_date,
    "action": str,
    "violation_code": str,
    "violation_description": str,
    "critical_flag": str,
    "int": str,
    "grade": str,
    "record_date": to_date,
    "grade_date": to_date,
    "inspection_type": str
}
restaurtant_col_names = [
    "camis",
    "dba",
    "boro",
    "building",
    "street",
    "zipcode",
    "phone",
    "cuisine_description"
]
inspection_col_names = [
    "restaurant_camis",
    "action",
    "critical_flag",
    "grade",
    "grade_date",
    "inspection_date",
    "inspection_type",
    "record_date",
    "score",
    "violation_code",
    "violation_description"
]
cursors = {
    list: psycopg2.extras.DictCursor,
    dict: psycopg2.extras.RealDictCursor
}


def connect():
    url = os.environ.get('DATABASE_URL', None)
    if url:
        url = urlparse(url)
        db = "dbname={} user={} password={} host={} ".format(
            url.path[1:],
            url.username,
            url.password,
            url.hostname
        )
    else:
        db = "dbname=great_thai user=postgres"
    return psycopg2.connect(db)


def execute(statement, vals={}, return_type=dict):
    cursor = cursors[return_type]
    with connect() as connection:
        with connection.cursor(cursor_factory=cursor) as cur:
            cur.execute(statement, vals)


def fetch_all(statement, vals={}, return_type=dict):
    cursor = cursors[return_type]
    with connect() as connection:
        with connection.cursor(cursor_factory=cursor) as cur:
            cur.execute(statement, vals)
            return cur.fetchall()
