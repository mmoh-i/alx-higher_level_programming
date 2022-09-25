-- Import the database dump from hbtn_0d_tvshows to MYSQLserver.
-- A script that lists all genres from hbtn_0d_tvshows and displays number of shows linked to each.
SELECT g.`name` AS genre, COUNT(g.`genre_id`) AS number_of_ahows
  FROM `tv_genres` AS g
       LEFT JOIN `tv_show__genres` AS g1
       ON g.`id` = g1.`show_id`
       WHERE g.genre_id` IS NULL
 ORDER BY genre;
