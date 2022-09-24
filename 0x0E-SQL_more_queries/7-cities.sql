--A script that creates the database htbn_0d_usa with table cities.
--(in the database hbtn_0d_usa)on MySqL.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.cities (
	PRIMARY KEY(`id`),
	FORIENG KEY(`state_id`) REFRENCES `hbtn_0d_usa`.`states`(`id`),
	`id`       INT	        NOT NULL AUTO_INCREMENT,
	`state_id` INT	        NOT NULL,
	`name`     VARCHAR(256) NOT NULL
);

