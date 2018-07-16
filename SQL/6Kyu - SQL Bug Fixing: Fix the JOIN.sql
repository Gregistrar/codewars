# My Solution

SELECT 
  j.job_title,
  ROUND(AVG(j.salary),2)::FLOAT as average_salary,
  COUNT(p.id) as total_people,
  ROUND(SUM(j.salary),2)::FLOAT as total_salary
  
FROM people AS p
  JOIN job AS j ON p.id = j.people_id 
GROUP BY j.job_title
ORDER BY average_salary DESC
