-- average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`VALUE`) AS `avg_temp`
  FROM `tempratures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
