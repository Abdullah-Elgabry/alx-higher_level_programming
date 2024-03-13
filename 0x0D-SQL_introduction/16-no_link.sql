-- this query will shows all records (not null)in second_table and order them in desc order.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;