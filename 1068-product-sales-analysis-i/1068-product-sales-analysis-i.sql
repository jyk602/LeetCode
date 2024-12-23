/* Write your T-SQL query statement below */
-- SELECT B.product_name, A.year, A.Price 
--   FROM Sales AS A 
--   JOIN Product AS B ON A.product_id = B.product_id 

SELECT 
    p.product_name, 
    s.year, 
    s.price
FROM 
    Sales s
JOIN 
    Product p ON s.product_id = p.product_id;