SELECT q1.person_name
FROM Queue q1
LEFT JOIN Queue q2
ON q1.person_id >= q2.person_id
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1