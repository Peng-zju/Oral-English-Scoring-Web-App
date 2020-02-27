CREATE DATABASE winter_proj_db;

USE winter_proj_db;

DROP TABLE IF EXISTS Region;
CREATE TABLE Region(
	rid INT NOT NULL,
	region_name VARCHAR(20) NOT NULL,
	PRIMARY KEY(rid)
);

DROP TABLE IF EXISTS QuestionBank;
CREATE TABLE QuestionBank(
	rid INT NOT NULL,
	type_id INT NOT NULL,
	type_name VARCHAR(20) NOT NULL,
	latest_ver DATETIME NOT NULL,
	PRIMARY KEY(rid, type_id),
	FOREIGN KEY(rid) REFERENCES Region(rid)
);

DROP TABLE IF EXISTS Question;
CREATE TABLE Question(
	rid INT NOT NULL,
	type_id INT NOT NULL,
	qid INT NOT NULL AUTO_INCREMENT,
	requirement VARCHAR(200) NOT NULL,
	body VARCHAR(2000) NOT NULL,
	comment VARCHAR(200),
	image VARCHAR(200),
	version DATETIME NOT NULL,
	PRIMARY KEY(qid),
	FOREIGN KEY (rid, type_id) REFERENCES QuestionBank(rid, type_id)
);

DROP TRIGGER IF EXISTS update_ver_trigger;
CREATE TRIGGER update_ver_trigger
AFTER INSERT ON Question
FOR EACH ROW
UPDATE QuestionBank Q SET Q.latest_ver = NEW.version WHERE Q.rid = NEW.rid AND Q.type_id = NEW.type_id; 
