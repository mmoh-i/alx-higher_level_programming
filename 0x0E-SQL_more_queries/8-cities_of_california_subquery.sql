-- A script that lists the cities of california that can be found.
-- in the dataase hbtn_0d_usa.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
	(SELECT `id` 
	  FROM `state`
	  where `name` = "Carlifornia")
 ORDER BY `id`;
