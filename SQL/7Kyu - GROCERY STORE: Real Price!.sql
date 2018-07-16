# My Solution

SELECT p.name
  , p.weight
  , p.price
  , ROUND((p.price*1000/weight)::numeric, 2)::float AS price_per_kg

FROM products AS p
ORDER BY price_per_kg, name ASC
