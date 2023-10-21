SELECT COUNT(custID), state
FROM customers
WHERE EXISTS(
    SELECT custID, orderID
    FROM orders
    WHERE EXISTS (
    
        SELECT orderID, itemID
        FROM lineitems
        WHERE EXISTS(
        
            SELECT itemID
            FROM items
            WHERE description = 'Umbrella' AND lineitems.itemID = items.itemID
        ) AND orders.orderID = lineitems.orderID
    ) AND customers.custID = orders.custID
)
GROUP BY state