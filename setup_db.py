from db_connection import execute


def setup_db():
    execute("""
        DROP TABLE IF EXISTS restaurants;
        CREATE TABLE restaurants (
            id serial PRIMARY KEY,
            camis varchar,
            dba varchar,
            boro varchar,
            building varchar,
            street varchar,
            zipcode varchar,
            phone varchar,
            cuisine_description varchar,
            inspection_date date,
            action varchar,
            violation_code varchar,
            violation_description varchar,
            critical varchar,
            score varchar,
            grade varchar,
            grade_date date,
            record_date date,
            inspection_type varchar
        );
        CREATE INDEX ON restaurants (grade);
    """)

setup_db()
