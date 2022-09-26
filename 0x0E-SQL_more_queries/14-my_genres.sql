-- Import the databasse dump from hbtn_0d_tvshows to MySQL.
-- A script that uses the hbtn_0d_tvshows database to lists all genres of show Dexter.
SELECT t.`name` AS `name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`
       
       INNER JOIN `tv_shows` AS t
       ON g.`id` = t.`id`
       WHERE t.`title` = 'Dexter'
  ORDER BY t.`name`;
