-- List all records in the table second)Table with a score >= 10.
SELECCT `score`, `name`
   FROM `second_table`
  WHERE `score` >= 10
ORDER BY `score` DESC;
