-- Import database dump form hbtn_0d_tvshows to MySQL.
-- A script that lists all comedy shows in the database.
SELECT t.`title`
 FROM `tv_shows` AS t
      INNER JOIN  `tv_shows_genres` AS s
      ON t.`id` = s.`show_id`
      
      INNER JOIN `tv_genres` AS g
      ON g.`id` = s.`genre_id`
      WHERE g.`name` = 'Comedy'
ORDER BY t.`title`
 
