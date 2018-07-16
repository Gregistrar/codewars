# My Solution

SELECT d.id
  , d.name

FROM departments AS d
WHERE EXISTS 
  (SELECT *
  FROM departments as d
  LEFT JOIN sales s
    ON d.id = s.department_id
    WHERE s.price >= 98.00)
