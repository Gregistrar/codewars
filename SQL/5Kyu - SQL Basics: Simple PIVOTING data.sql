# My Solution

CREATE EXTENSION tablefunc;

SELECT *
FROM crosstab( 
  'SELECT p.name, detail, COUNT(d.id)
  FROM products AS p
  JOIN details AS d
    ON p.id = d.product_id
  GROUP BY p.name, detail
  ORDER BY 1,2'
) AS newtable(
      name TEXT
      , bad bigint
      , good bigint
      , ok bigint)
GROUP BY name, good, ok, bad
ORDER BY name 
