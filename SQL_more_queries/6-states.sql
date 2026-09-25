-- Create database hbtn_0d_usa and table states
-- Creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch context to the target database
USE hbtn_0d_usa;
-- Creates the states table with auto-increment primary key
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
