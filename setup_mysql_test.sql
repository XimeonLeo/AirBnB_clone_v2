-- A script that prepares MySQL database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a user IN localhost
CREATE USER IF NOT 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting all permission to user on this database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'
