from db_connection import execute
from query_helpers import add_indices


def setup_db():
    execute("""
        DROP TABLE IF EXISTS restaurants;
        CREATE TABLE restaurants (
            id serial PRIMARY KEY,
            camis int,
            dba varchar,
            boro varchar,
            building varchar,
            street varchar,
            zipcode varchar,
            phone varchar,
            cuisine_description varchar
        );
        DROP TABLE IF EXISTS inspections;
        CREATE TABLE inspections (
            id serial PRIMARY KEY,
            restaurant_camis int,
            inspection_date date,
            action varchar,
            violation_code varchar,
            violation_description varchar,
            critical_flag varchar,
            score varchar,
            grade varchar,
            grade_date date,
            record_date date,
            inspection_type varchar
        );
    """)
    add_indices()

setup_db()
