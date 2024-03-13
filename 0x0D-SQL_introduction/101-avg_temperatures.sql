-- this query will calculate the avg temperature by cite ordered by temp descending
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;