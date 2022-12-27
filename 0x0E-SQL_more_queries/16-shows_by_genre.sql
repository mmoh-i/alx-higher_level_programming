-- Import the database dump from hbtn_0d_tvshows to MySQL server.
--  A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT t.`title`, s.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres`AS g
       ON t.`id` = g.`show_id`
       
       LEFT JOIN `tv_genres` AS s
       ON g.`genre_id` = s.`id`
 ORDER BY t.`title`, s.`name`
