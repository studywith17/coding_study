# https://school.programmers.co.kr/learn/courses/30/lessons/131124

sql = '''
SELECT MP.MEMBER_NAME,
       RR.REVIEW_TEXT, 
       DATE_FORMAT(RR.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE MP JOIN REST_REVIEW RR ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE RR.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW RR
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(MEMBER_ID) DESC
                     LIMIT 1)
ORDER BY RR.REVIEW_DATE, RR.REVIEW_TEXT
'''