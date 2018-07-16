# My Solution

SELECT id
  , hours
  , FLOOR(hours::float*0.5) AS liters

FROM cycling
