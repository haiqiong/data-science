import sqlite3
import sys

conn = sqlite3.connect('./reuters.db')
cursor = conn.cursor()

selectSql = """
SELECT count(*)
FROM frequency f
WHERE f.docid = '10398_txt_earn'
"""

with open('./select.txt', 'w') as selectFile:
    for item in cursor.execute(selectSql):
    #print item[0]
    #select.write(str(item[0]))
        #print(item[0], file = selectFile)
        selectFile.write(str(item[0]))

projectSql = """
SELECT count(f.term)
FROM frequency f
WHERE f.docid = '10398_txt_earn' 
AND f.count = 1
"""

with open('./select_project.txt', 'w') as projectFile:
    for item in cursor.execute(projectSql):
        projectFile.write(str(item[0]))
        
unionSql = """
SELECT count(*)
FROM (
SELECT f1.term
FROM frequency f1
WHERE f1.docid = '10398_txt_earn'
AND f1.count = 1
UNION
SELECT f2.term
FROM frequency f2
WHERE f2.docid = '925_txt_trade'
AND f2.count = 1
) u
"""

with open('./union.txt', 'w') as unionFile:
    for item in cursor.execute(unionSql):
        unionFile.write(str(item[0]))
        
countSql = """
SELECT count (*)
FROM (
SELECT DISTINCT f.docid
FROM frequency f
WHERE f.term LIKE 'parliament'
GROUP BY f.docid
)
"""

with open('./count.txt', 'w') as countFile:
    for item in cursor.execute(countSql):
        countFile.write(str(item[0]))
        #print item[0]
        
bigdocSql = """
SELECT count(*)
FROM (
SELECT f.docid
FROM frequency f
GROUP BY f.docid
HAVING SUM(f.count) > 300
)
"""

with open('./big_documents.txt', 'w') as bigDocFile:
    for item in cursor.execute(bigdocSql):
        bigDocFile.write(str(item[0]))
        #print item[0]
        
twoWordSql = """
SELECT count(t.docid)
FROM (
SELECT DISTINCT f1.docid
FROM frequency f1
WHERE f1.term LIKE 'transactions'
) as t
WHERE t.docid IN (
SELECT DISTINCT f2.docid
FROM frequency f2
WHERE f2.term LIKE 'world'
)
/*
SELECT count(*)
FROM (
SELECT DISTINCT f1.docid
FROM frequency f1
WHERE f1.term LIKE 'transactions'
) as t
INNER JOIN (
SELECT DISTINCT f2.docid
FROM frequency f2
WHERE f2.term LIKE 'world'
) as w
ON t.docid = w.docid
*/
"""

with open('./two_words.txt', 'w') as twoWordsFile:
    for item in cursor.execute(twoWordSql):
        twoWordsFile.write(str(item[0]))
        print item[0]


        
