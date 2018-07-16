# My Solution

SELECT f.name
  , SUM(f.won::int) AS won
  , SUM(f.lost::int) AS lost

FROM fighters AS f
LEFT JOIN winning_moves AS wm
  ON wm.id = f.move_id
  
WHERE NOT wm.move IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY f.name
ORDER BY won DESC
LIMIT 6
