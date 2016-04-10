__author__ = 'Alexey'
from algorithms.disjoint_set_structure import init_data, unite
from algorithms import disjoint_set_structure as dss

logfile = open("log.txt")
persons = logfile.readline().strip().split(' ')

init_data(persons)

data = []
while dss.sets_count > 1:
    line = logfile.readline().strip()
    if len(line) == 0:
        print 'Seems like your log is not full or your users are not connected. :C sorry'
    data = line.split(' ')
    person_1 = data[2]
    person_2 = data[3]
    unite(person_1, person_2)

print 'All users connected at: ' + data[0] + ' ' + data[1]
