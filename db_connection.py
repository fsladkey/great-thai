import os
import psycopg2
import psycopg2.extras
import datetime
DB_NAME = os.environ.get("DATABASE_URL", "great_thai")


def to_date(string_formatted_date):
    """Parse data in the format of mm/dd/yyyy into datatime object"""
    return datetime.datetime.strptime(string_formatted_date, "%m/%d/%Y")

col_types = {
    "camis": str,
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
    "score": str,
    "grade": str,
    "record_date": to_date,
    "grade_date": to_date,
    "inspection_type": str
}
col_names = [
    "camis",
    "dba",
    "boro",
    "building",
    "street",
    "zipcode",
    "phone",
    "cuisine_description",
    "inspection_date",
    "action",
    "violation_code",
    "violation_description",
    "critical_flag",
    "score",
    "grade",
    "record_date",
    "grade_date",
    "inspection_type",
]
cursor_factory = psycopg2.extras.RealDictCursor


def connect(db):
    return psycopg2.connect("dbname={db} user=postgres".format(db=db))


def execute(statement, vals={}):
    with connect(DB_NAME) as connection:
        with connection.cursor(cursor_factory=cursor_factory) as cur:
            cur.execute(statement, vals)


def fetch(statement, vals={}):
    with connect(DB_NAME) as connection:
        with connection.cursor(cursor_factory=cursor_factory) as cur:
            cur.execute(statement, vals)
            return cur.fetchone()


def fetch_all(statement, vals={}):
    with connect(DB_NAME) as connection:
        with connection.cursor(cursor_factory=cursor_factory) as cur:
            cur.execute(statement, vals)
            return cur.fetchall()
