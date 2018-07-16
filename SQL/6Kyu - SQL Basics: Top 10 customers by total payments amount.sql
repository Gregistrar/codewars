# My Solution

SELECT c.customer_id
  , c.email
  , COUNT(p.customer_id) AS payments_count
  , CAST(SUM(p.amount) as float) AS total_amount
 
 FROM customer c
 LEFT JOIN payment p
   ON c.customer_id = p.customer_id

GROUP BY c.customer_id
ORDER BY total_amount DESC
LIMIT 10;
