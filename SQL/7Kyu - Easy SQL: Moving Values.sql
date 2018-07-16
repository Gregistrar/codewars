# My Solution

SELECT char_length(name) AS id
  , char_length(legs::text) AS name
  , char_length(arms::text) AS legs
  , char_length(characteristics) AS arms
  , char_length(id::text) AS characteristics

FROM monsters
