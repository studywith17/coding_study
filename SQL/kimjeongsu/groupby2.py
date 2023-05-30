# https://school.programmers.co.kr/learn/courses/30/lessons/131116

sql = '''
SELECT category, price AS max_price, product_name
FROM food_product
WHERE (category,price) IN (
    SELECT category, MAX(price) AS max_price
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category
)
ORDER BY 2 DESC
'''