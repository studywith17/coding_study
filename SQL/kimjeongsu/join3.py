# https://school.programmers.co.kr/learn/courses/30/lessons/133027

sql = '''
SELECT FLAVOR
FROM (
    SELECT H.FLAVOR, SUM(H.TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF H LEFT JOIN JULY J ON H.FLAVOR = J.FLAVOR
    GROUP BY H.FLAVOR
    UNION ALL
    SELECT J.FLAVOR, SUM(J.TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF H RIGHT JOIN JULY J ON H.FLAVOR = J.FLAVOR
    GROUP BY J.FLAVOR
) AS subquery
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3
'''