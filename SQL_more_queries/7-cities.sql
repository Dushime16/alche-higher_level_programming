-- Create database hbtn_0d_usa and table cities
-- Creates the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch database execution context
USE hbtn_0d_usa;
-- Creates the cities table with a foreign key linking to states
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
