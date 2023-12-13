# Write your MySQL query statement below
SELECT
(SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary


-- Option 2
SELECT  MAX(SALARY) AS SecondHighestSalary
FROM EMPLOYEE
WHERE SALARY <> (SELECT MAX(SALARY) FROM EMPLOYEE);