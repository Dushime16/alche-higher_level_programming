-- List all cities of California in the database hbtn_0d_usa
-- This script filters records using a subquery instead of a JOIN keyword
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
