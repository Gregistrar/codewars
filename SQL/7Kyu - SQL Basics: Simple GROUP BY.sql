# My Solution

SELECT age
  , COUNT(people) AS people_count

FROM people

GROUP BY age
