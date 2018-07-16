# My Solution

SELECT products.*
  , c.name AS company_name

FROM products
LEFT JOIN companies AS c
ON products.company_id = c.id;
