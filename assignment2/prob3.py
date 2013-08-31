import sqlite3
import sys

conn = sqlite3.connect('./reuters.db')
cursor = conn.cursor()

productSql = """
/*FROM (
SELECT m1.docid as source, 
m2.docid as target, sum(m1.count * m2.count) as product
*/
SELECT sum(m1.count * m2.count) 
FROM (
SELECT f3.docid, f3.term, f3.count
FROM frequency f3
WHERE f3.docid = '10080_txt_crude'
) m1
INNER JOIN (
SELECT tmp.term, tmp.docid, tmp.count
FROM(
SELECT f2.term, f1.docid, f1.count
FROM frequency f1
INNER JOIN frequency f2
ON f1.term = f2.term
GROUP BY f1.docid, f2.term
) tmp
WHERE tmp.docid = '17035_txt_earn'
) m2
ON m1.term= m2.term
WHERE m1.docid < m2.docid
GROUP BY m1.docid, m2.docid
/*
) r

WHERE r.source = '10080_txt_crude'
AND r.target = '17035_txt_earn' */
"""

simSql = """
SELECT tmp.product
FROM (
SELECT m1.docid, m3.docid, sum(m1.count * m3.count) as product
FROM frequency m1
INNER JOIN 
(SELECT m2.term, m1.docid, m1.count
FROM frequency m1
INNER JOIN frequency m2
ON m1.term = m2.term
GROUP BY m1.docid, m2.term
) m3
ON m1.term = m3.term
GROUP BY m1.docid, m3.docid
) tmp
WHERE tmp.docid = '10080_txt_crude'
AND tmp.docid = '17035_txt_earn'
"""

"""
simSql = 
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
with open('./similarity_matrix.txt', 'w') as multiplyFile:
    for (s, t, sim) in cursor.execute(simSql):
        multiplyFile.write(str(sim))
        print s, t, sim

