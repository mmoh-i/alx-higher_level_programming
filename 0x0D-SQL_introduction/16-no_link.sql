-- a script that lists all records of the table secon_table of the database htbn_0c_0
SELECT `score`, `name`
  FROM `second_table`
 WHERE `name` != ""
ORDER BY `score` DESC;
