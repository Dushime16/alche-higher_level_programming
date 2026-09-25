-- Create the table id_not_null on the MySQL server
-- The table contains an id with a default value of 1, and a name
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
