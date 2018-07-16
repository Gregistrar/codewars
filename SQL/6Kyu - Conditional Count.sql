# My Solution

SELECT EXTRACT(MONTH FROM payment_date) AS month
  , COUNT(payment_id) AS total_count
  , CAST(SUM(amount) as decimal) AS total_amount
  , COUNT(CASE WHEN staff_id = 1 THEN payment_id
      ELSE NULL END) AS mike_count
  , CAST(SUM(CASE WHEN staff_id = 1 THEN amount
      ELSE NULL END) AS decimal) AS mike_amount
  , COUNT(CASE WHEN staff_id = 2 THEN payment_id
      ELSE NULL END) AS jon_count
  , CAST(SUM(CASE WHEN staff_id = 2 THEN amount
      ELSE NULL END) AS decimal) AS jon_amount

FROM payment
GROUP BY month
ORDER BY month ASC
