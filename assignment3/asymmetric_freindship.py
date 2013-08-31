import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    if (record[0] <= record[1]):
        key = record[0] + '_' + record[1]
    else:
        key = record[1] + '_' + record[0]
    mr.emit_intermediate(key, (record[0], record[1]))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if (len(list_of_values) == 1):
        (person, friend) = list_of_values[0]
        mr.emit(((person, friend)))
        mr.emit(((friend, person)))
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
