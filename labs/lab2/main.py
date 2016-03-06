__author__ = 'Alexey'
from graph_tools.graph_builder import build_random_graph
from graph_tools.common_utils import sort_graph_adjacency, shuffle_adjacency

n = input("Enter vertices number: ")
p = input("Enter probability: ")

if type(n) != int or type(p) != float:
    print "Your input is invalid, sorry :C Try again?"
    exit(1)

vertices, adjacency = build_random_graph(n, p)
adjacency = shuffle_adjacency(adjacency)
print('Shuffled: ' + str(adjacency))
adjacency = sort_graph_adjacency(adjacency)
print('Sorted: ' + str(adjacency))
