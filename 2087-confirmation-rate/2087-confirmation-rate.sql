/* Write your T-SQL query statement below */
SELECT S.user_id,
       ROUND(AVG(CASE WHEN C.ACTION ='confirmed' THEN 1.00 ELSE 0 END),2) AS confirmation_rate
  FROM Signups AS S
  LEFT JOIN Confirmations AS C ON C.USER_ID = S.USER_ID 
  GROUP BY S.USER_ID

  
