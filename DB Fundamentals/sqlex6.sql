
SELECT lineitems.itemID, lineitems.quantity, items.description
FROM `lineitems`
LEFT JOIN items ON lineitems.itemID = items.itemID
WHERE lineitems.quantity = (SELECT MAX(lineitems.quantity) FROM lineitems)