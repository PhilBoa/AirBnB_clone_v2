-- Create the database if it's not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user if it's not exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db database to the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the
-- hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

