-- A script that prepares MySQL database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a user IN localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhos' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting all permission to user on this database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'
