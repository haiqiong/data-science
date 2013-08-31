import sqlite3
import sys

conn = sqlite3.connect('./mydb.db')
cursor = conn.cursor()

sql = """
SELECT m.row_num, m.col_num, m.value 
FROM matrix m
"""
print 'matrix:'
for (row, col, value) in cursor.execute(sql):
    print row, col, value
 
print 'product:' 
productSql = """
SELECT m1.row_num, m2.col_num, sum(m1.value * m2.value)
FROM matrix m1
INNER JOIN matrix m2
ON m1.col_num = m2.row_num
GROUP BY m1.row_num, m2.col_num
"""

for (row, col, value) in cursor.execute(productSql):
    print row, col, value 
    
print 'transpose:'

tranSql = """
SELECT m2.col_num, m1.row_num, m1.value
FROM matrix m1
INNER JOIN matrix m2
ON m1.col_num = m2.col_num
GROUP BY m1.row_num, m2.col_num
"""
for (row, col, value) in cursor.execute(tranSql):
    print row, col, value 
    

simSql = """
SELECT m1.row_num, m3.row_num, sum(m1.value * m3.value)
FROM matrix m1
INNER JOIN 
(SELECT m2.col_num, m1.row_num, m1.value
FROM matrix m1
INNER JOIN matrix m2
ON m1.col_num = m2.col_num
GROUP BY m1.row_num, m2.col_num
) m3
ON m1.col_num = m3.col_num
GROUP BY m1.row_num, m3.row_num
"""

simSql1 = """
SELECT m1.row_num, m3.row_num, sum(m1.value * m3.value)
FROM (
SELECT f4.row_num, f4.col_num, f4.value
FROM matrix f4
WHERE f4.row_num = 0
) m1
INNER JOIN 
(SELECT tmp.col_num, tmp.row_num, tmp.value
FROM(
SELECT m2.col_num, m1.row_num, m1.value
FROM matrix m1
INNER JOIN matrix m2
ON m1.col_num = m2.col_num
GROUP BY m1.row_num, m2.col_num
) tmp
WHERE tmp.row_num = 3
) m3
ON m1.col_num = m3.col_num
GROUP BY m1.row_num, m3.row_num
"""

print 'sim:'
for (row, col, value) in cursor.execute(simSql):
    print row, col, value 
    
print 'sim1:'
for (row, col, value) in cursor.execute(simSql1):
    print row, col, value 