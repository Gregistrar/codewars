WITH good AS (
SELECT p.id
  , p.name
  , detail AS good
  , COUNT(d.detail) AS good_count

FROM products AS p
JOIN details AS d
  ON p.id = d.product_id
WHERE detail = 'good'
GROUP BY p.id, p.name, detail
ORDER BY name
),
ok AS (
SELECT p.id
  , p.name
  , detail AS ok
  , COUNT(d.detail) AS ok_count

FROM products AS p
JOIN details AS d
  ON p.id = d.product_id
WHERE detail = 'ok'
GROUP BY p.id, p.name, detail
ORDER BY name
),
bad AS (
SELECT p.id
  , p.name
  , detail AS bad
  , COUNT(d.detail) AS bad_count

FROM products AS p
JOIN details AS d
  ON p.id = d.product_id
WHERE detail = 'bad'
GROUP BY p.id, p.name, detail
ORDER BY name
)

SELECT g.name
  , g.good_count AS good
  , o.ok_count AS ok
  , b.bad_count AS bad
FROM good AS g
LEFT JOIN ok AS o
  ON g.id  = o.id
LEFT JOIN bad as b
  ON o.id = b.id
ORDER BY g.name
