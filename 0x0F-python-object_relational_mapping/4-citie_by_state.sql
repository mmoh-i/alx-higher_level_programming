--creatig table to test for cities_by_state task
CREATE DATABASE
    IF NOT EXISTS `hbtn_0e_4_usa`
CREATE TABLE IF NOT EXISTS `hbtn_0e_4_usa`.`states` (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
INSERT INTO `states` (name) VALUES ("California"), ("Ariozona"), ("Texas"), ("New York", ("Nevada");

CREATE TABLE IF NOT EXISTS `hbtn_0e_4_usa`.`cities` (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(state_id)
	);
INSERT INTO `cities` (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
