--import databae dump from hbtn_0d_tvshows to mysql.
--A script that lists all shows contained in hbtn_0d_tvshows that have at list one genred linked.
SELECT t.`title`, g.`genre_id`
  FROM `tv_show` AS t
 INNER JOIN `tv_show_genres` AS g
    ON t.`id` = g.`show_id`
 ORDER BY t.`title`, g.`genre_id`;
