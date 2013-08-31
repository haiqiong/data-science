import sqlite3
import sys

conn = sqlite3.connect('./matrix.db')
cursor = conn.cursor()

productSql = """
SELECT r.product
FROM (
SELECT m1.row_num, m2.col_num, sum(m1.value * m2.value) as product
FROM A m1
INNER JOIN B m2
ON m1.col_num = m2.row_num
GROUP BY m1.row_num, m2.col_num
) r
WHERE r.row_num = 2
AND r.col_num = 3
"""

with open('./multiply.txt', 'w') as multiplyFile:
    for item in cursor.execute(productSql):
        multiplyFile.write(str(item[0]))
        print item[0]

