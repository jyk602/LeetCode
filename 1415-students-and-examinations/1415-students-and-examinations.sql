/* Write your T-SQL query statement below */
SELECT a.student_id
     , a.student_name
     , s.subject_name
     , COUNT(b.student_id) AS attended_exams
  FROM Students AS a
  CROSS JOIN Subjects AS s
  LEFT JOIN Examinations AS b ON a.student_id = b.student_id AND s.subject_name = b.subject_name 
  GROUP BY a.student_id, a.student_name, s.subject_name
  ORDER BY a.student_id, s.subject_name
