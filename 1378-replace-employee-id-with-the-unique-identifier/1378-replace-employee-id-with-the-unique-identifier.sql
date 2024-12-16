/* Write your T-SQL query statement below */
SELECT B.unique_id, A.name 
  FROM Employees AS A 
  LEFT JOIN EmployeeUNI AS B ON B.id = A.id 
  