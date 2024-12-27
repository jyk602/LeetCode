/* Write your T-SQL query statement below */
SELECT a.machine_id, ROUND(AVG(b.timestamp-a.timestamp),3) as processing_time
  FROM Activity AS a
  JOIN Activity AS b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
 WHERE a.activity_type = 'start' AND b.activity_type = 'end' 
  GROUP BY a.machine_id  


-- SELECT 
-- a.machine_id, 
-- ROUND(
--     (SELECT AVG(a1.timestamp) FROM Activity AS a1 WHERE a1.activity_type ='end' AND a1.machine_id = a.machine_id) - 
--     (SELECT AVG(a1.timestamp) FROM Activity AS a1 WHERE a1.activity_type ='start' AND a1.machine_id = a.machine_id),3) as processing_time
--   FROM Activity AS a 
--   GROUP BY a.machine_id