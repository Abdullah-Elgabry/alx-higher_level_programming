-- this query will prints all the cities of California founded in the hbtn_0d_usa db
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
