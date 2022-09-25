-- Import the database dump from hbtn_0d_tvshows to MYSQLserver.
-- A script that lists all genres from hbtn_0d_tvshows and displays number of shows linked to each.
SELECT 
    g.`name` AS `genre`, 
    COUNT(*) AS `number_of_shows`
    FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS g1
       ON g.`id` = g1.`genre_id`
       WHERE g.`genre_id` IS NULL
 GROUP BY genre
 ORDER BY `number_of_show` DESC;
