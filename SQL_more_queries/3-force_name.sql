-- Create the table force_name on the MySQL server
-- The table contains an id and a name that cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
