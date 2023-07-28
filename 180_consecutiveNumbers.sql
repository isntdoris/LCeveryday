# Write your MySQL query statement below
with cte as (
    SELECT num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    FROM logs
)

SELECT DISTINCT num ConsecutiveNums
FROM cte
WHERE (num=num1) AND (num=num2)