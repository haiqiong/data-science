import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    l = 5; n = 5
    if record[0] == 'a':
        for k in range(n):
            mr.emit_intermediate((record[1], k), (record[2], record[3]))
    elif record[0] == 'b':
        for k in range(l):
            mr.emit_intermediate((k, record[2]), (record[1], record[3]))


def reducer(key, list_of_values):
    sum = 0
    product = {}
    print 'key:', key
    print 'value:', list_of_values
    for (j, value) in list_of_values:
        if j in product:
            sum = sum + product[j] * value
        else:
            product[j] = value
  
    mr.emit((key[0], key[1], sum))
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
