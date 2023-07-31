SELECT
CASE
    WHEN id % 2 <> 0 AND id = (SELECT COUNT(*) FROM Seat) THEN s.id
    WHEN id % 2 = 1 THEN s.id + 1
    ELSE s.id - 1

    END AS id,
    student

FROM Seat s
ORDER BY id