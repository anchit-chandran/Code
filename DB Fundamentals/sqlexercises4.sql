SELECT COUNT(DISTINCT custID), state
FROM customers
GROUP BY state