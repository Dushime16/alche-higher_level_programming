-- List all cities contained in the database hbtn_0d_usa
-- This script joins cities and states displaying cities.id, cities.name, and states.name
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
