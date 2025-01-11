/* Write your T-SQL query statement below */

SELECT e1.name
  FROM Employee AS e1
  JOIN (SELECT managerId, COUNT(*) AS cntReports
          FROM Employee 
        GROUP BY managerId
        HAVING COUNT(*) >= 5
    ) AS e2 ON e1.id = e2.managerId

