SELECT COUNT(DISTINCT custID)
FROM orders
WHERE EXISTS 
	(
    SELECT orderID, quantity
    FROM lineitems
    WHERE (quantity > 2) AND orders.orderID = lineitems.orderID
    )