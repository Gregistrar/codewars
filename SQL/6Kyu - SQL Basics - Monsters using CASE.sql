# My Solution

SELECT th.id
  , th.heads
  , bh.legs
  , th.arms
  , bh.tails
  , CASE WHEN heads > arms OR tails > legs THEN 'BEAST'
    ELSE 'WEIRDO' END AS species

FROM top_half AS th
JOIN bottom_half AS bh
  ON th.id = bh.id
ORDER BY species
