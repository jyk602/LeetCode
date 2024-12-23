/* Write your T-SQL query statement below */
-- SELECT b.product_name, a.year, a.price 
--   FROM Sales a 
--   JOIN Product b ON a.product_id = b.product_id;

SELECT 
    p.product_name, 
    s.year, 
    s.price
FROM 
    Sales s
JOIN 
    Product p ON s.product_id = p.product_id;