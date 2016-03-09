__author__ = 'Alexey'
from algorithms.exponential_algorithms import calculate_branching_multiplier

for i in range(1, 7):
    for j in range(1, 7):
        print '%.4f' % calculate_branching_multiplier([i, j]),
    print
