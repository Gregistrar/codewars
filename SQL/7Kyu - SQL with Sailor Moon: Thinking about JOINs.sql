# My Solution

SELECT ss.senshi_name AS sailor_senshi
  , ss.real_name_jpn AS real_name
  , c.name AS cat
  , sch.school

FROM sailorsenshi AS ss
LEFT JOIN cats AS c
  ON c.id = ss.cat_id
LEFT JOIN schools AS sch
  ON sch.id = ss.school_id
