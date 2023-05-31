# https://school.programmers.co.kr/learn/courses/30/lessons/131117

sql='''
SELECT P.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT P JOIN FOOD_ORDER O ON P.PRODUCT_ID=O.PRODUCT_ID
WHERE MONTH(O.PRODUCE_DATE)='5'
GROUP BY P.PRODUCT_ID, P.PRODUCT_NAME
ORDER BY 3 DESC, 1
'''