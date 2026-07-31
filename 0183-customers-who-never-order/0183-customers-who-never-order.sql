SELECT
    c.name as Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 
        o.customerId
    FROM Orders o
    WHERE o.customerId = c.id
)