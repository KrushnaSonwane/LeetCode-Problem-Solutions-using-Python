# Write your MySQL query statement below
WITH first AS(
    SELECT
        u.name as results,
        COUNT(*) as cnt
    FROM Users u
    JOIN MovieRating mr
    ON mr.user_id = u.user_id
    GROUP BY u.user_id
    ORDER BY 2 DESC, 1 ASC
    LIMIT 1
),
second AS(
    SELECT
        m.title as results,
        AVG(mr.rating)
    FROM Movies m
    JOIN MovieRating mr
    ON m.movie_id = mr.movie_id AND YEAR(mr.created_at) = 2020 AND MONTH(mr.created_at) = 2
    GROUP BY mr.movie_id
    ORDER BY 2 DESC, 1 ASC
    LIMIT 1
)

SELECT
    results
FROM first
UNION ALL
SELECT results
FROM second