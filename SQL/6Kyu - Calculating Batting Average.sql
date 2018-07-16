# My Solution

SELECT player_name
  , games
  , CAST(ROUND((hits*1.0)/(at_bats*1.0), 3) AS text) AS batting_average

FROM yankees
WHERE at_bats >= 100
ORDER BY batting_average DESC
