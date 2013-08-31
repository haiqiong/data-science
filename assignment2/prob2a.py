import sqlite3
import sys

conn = sqlite3.connect('./mydb.db')
cursor = conn.cursor()

#cursor.execute("DROP TABLE matrix")

#create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS matrix
(/*id int AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE, */
row_num int, 
col_num int, 
value int)
""")

#insert multiple records using the more secure "?" method
"""values = [(0, 1, 2),
          (0, 2, -1),
          (1, 0, 1),
          (1, 1, 1),
          (1, 2, 2),
          (2, 0, 1),
          (2, 2, 3)]
          """
values = [(0, 1, 2),
          (0, 2, -1),
          (1, 0, 1),
          (2, 2, -3)]
cursor.executemany("INSERT INTO matrix VALUES(?, ?, ?)", values)

conn.commit()



