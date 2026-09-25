-- Create the table unique_id on the MySQL server
-- The table features a unique id with a default value of 1, and a name
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
