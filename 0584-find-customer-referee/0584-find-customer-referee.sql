/* Write your T-SQL query statement below */
SELECT name 
  FROM Customer 
 WHERE referee_Id <> 2 OR referee_id IS NULL; 