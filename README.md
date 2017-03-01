# Great Thai

[Live site on heroku](https://great-thai.herokuapp.com/)

To start the app locally, run the start script `./start.sh`.
It will take a few minutes to populate the database.

## Schema

I chose to split the data into two tables 'restaurants' and 'inspections'.
I did this to make it easier to get data per restaurant. The inspections table
has a separate record for each violation, so it could be further split up into
'inspection' and 'violations' but I decided not to do this because there
wasn't a clear unique identifier for the inspection (potentially date) and
I could query effectively for the data I was looking for either way.

### Restaurants

column name            | data type  | details
-----------------------|------------|---------
id                     | integer pk | (could potentially use camis)
camis                  | integer    | indexed
dba                    | varchar    |
boro                   | varchar    |
building               | varchar    |
street                 | varchar    |
zipcode                | varchar    |
phone                  | varchar    |
cuisine_description    | varchar    | indexed

### Inspections

column name            | data type  | details
-----------------------|------------|---------
restaurant_camis       | integer    | indexed - references restaurant.camis
inspection_date        | date       |
action                 | varchar    |
violation_code         | varchar    |
violation_description  | varchar    |
critical_flag          | varchar    |
score                  | varchar    | indexed
grade                  | varchar    | indexed
record_date            | date       | indexed
grade_date             | date       |
inspection_type        | varchar    |

## Top Ten Thai Restaurants

Here's the query I wrote to fetch the top ten Thai restaurants with a grade of B or higher.
It was deceptively complex because there are multiple inspections per restaurant.
I ran a self join on inspections to remove all but the latest. Since there are
multiple violations per day, I'm summing the violation scores to get a useful value
to order by after the grade. The flask app exposes an api endpoint to run this
query for any cuisine.

```sql
SELECT
  restaurants.*,
  max(inspections.grade) AS worst_grade,
  SUM(CAST(inspections.score AS integer)) AS total_score
FROM
  restaurants
JOIN
  inspections ON restaurants.camis = inspections.restaurant_camis
LEFT OUTER JOIN
  inspections as latest ON (latest.restaurant_camis = inspections.restaurant_camis AND
  inspections.record_date < latest.record_date)
WHERE
  cuisine_description = 'Thai' AND
  inspections.grade <= 'B' AND
  latest.record_date IS NULL
GROUP BY
  restaurants.id
ORDER BY
  max_grade, total_score
LIMIT
 10
 ```

I had a lot of fun with this and I'm looking forward to feedback. Thank you!
