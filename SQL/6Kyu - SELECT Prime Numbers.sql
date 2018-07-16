# My Solution

WITH x AS (
  SELECT * FROM generate_series( 2, 100 ) x
)
SELECT x.x AS prime
FROM x
WHERE NOT EXISTS (
  SELECT 1 FROM x y
  WHERE x.x > y.x AND x.x % y.x = 0)
ORDER BY prime asc
