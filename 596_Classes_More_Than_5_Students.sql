# Write your MySQL query statement below
# SELECT DISTINCT c.class
# FROM Courses c
# INNER JOIN (
#     SELECT class, COUNT(student) AS cnt
#     FROM Courses
#     GROUP BY 1
# ) tmp
# ON c.class = tmp.class
# WHERE tmp.cnt >= 5

SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(student) >= 5
;