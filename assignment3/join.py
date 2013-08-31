import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):  
    #if (len(list_of_values) == 2):
    order = []
    line = []
    for value in list_of_values:
        if value[0] == 'order':
            order.append(value)
        if value[0] == 'line_item':
            line.append(value)
    
    for orderRecord in order:
        for lineRecord in line:
            mixRec = []
            mixRec.extend(orderRecord)             
            mixRec.extend(lineRecord)
            mr.emit((mixRec))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
