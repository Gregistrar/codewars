# My Solution

SELECT *

FROM students

WHERE (quality1 = 'evil' and quality2 = 'cunning')
  OR (quality1 = 'brave' and quality2 NOT LIKE 'evil')
  OR (quality1 = 'studious' OR quality2 = 'intelligent')
  OR (quality1 = 'hufflepuff' OR quality2 = 'hufflepuff')
