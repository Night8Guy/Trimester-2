-- lists all cities of California contained in the database hbtn_0e_4_usa
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY id ASC;