4. SELECT * FROM users WHERE age BETWEEN 20 AND 30;
5. DELETE FROM users WHERE name LIKE '张'
6. SELECT AVG(age) AS average_age FROM users;
7. SELECT * FROM user WHERE name LIKE '张' AND age BETWEEN 20 AND 30 ORDER BY age DESC;
9. SELECT u.* FROM score s
JOIN team t ON s.teamid = t.id
JOIN user u ON s.userid = u.id
WHERE t.teamName = 'ECNU' AND u.age < 20;
10. SELECT COALESCE(SUM(score), 0) AS total_score
FROM score s
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU';