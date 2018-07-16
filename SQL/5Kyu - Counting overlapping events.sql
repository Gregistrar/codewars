# My Solution

SELECT v1.entry_time when_happened
  , COUNT(*) visits_count 

FROM visits v1 
JOIN visits v2 
  ON v1.entry_time >= v2.entry_time 
  AND v1.entry_time < v2.exit_time
GROUP BY v1.id
ORDER BY visits_count desc
LIMIT 1
