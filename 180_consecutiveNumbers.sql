# Write your MySQL query statement below
WITH cte AS (
    SELECT num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    FROM logs
)

SELECT DISTINCT num ConsecutiveNums
FROM cte
WHERE (num=num1) AND (num=num2)

-- Editorial Solution
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;