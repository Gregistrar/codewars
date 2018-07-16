# My Solution

SELECT CASE WHEN number1 = null THEN 0 ELSE ABS(number1) END AS abs
  , LOG(64, number2) AS log

FROM decimals
