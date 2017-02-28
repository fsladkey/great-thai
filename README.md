# Great Thai

To start the app locally, run the start script `./start.sh`.
It will take a few minutes to populate the database.

## Restaurants Schema

column name            | data type  | details
-----------------------|------------|---------
id                     | integer pk | duplicate to ensure unique key (camis is already unique)
camis                  | integer    |
dba                    | varchar    |
boro                   | varchar    |
building               | varchar    |
street                 | varchar    |
zipcode                | varchar    |
phone                  | varchar    |
cuisine_description    | varchar    | indexed
inspection_date        | date       |
action                 | varchar    |
violation_code         | varchar    |
violation_description  | varchar    |
critical_flag          | varchar    |
score                  | varchar    | indexed
grade                  | varchar    | indexed
record_date            | date       |
grade_date             | date       |
inspection_type        | varchar    |
