# My Solution

SELECT COUNT(name) AS products
  , country

FROM products
WHERE country IN ('United States of America', 'Canada')
GROUP BY country
ORDER BY products DESC
