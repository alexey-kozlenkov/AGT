__author__ = 'Alexey'

from graph_tools.graph_builder import build_connected_grpah
from graph_tools.graph_drawer import draw_graph
from graph_tools.common_utils import init_random_weights
from algorithms.algorithms import build_minimum_spanning_tree
import labs.lab3.disjoint_set_structure as dss

n = input("Enter vertices number: ")
p = input("Enter probability: ")

if type(n) != int or type(p) != float:
    print "Your input is invalid, sorry :C Try again?"
    exit(1)

vertices, adjacency = build_connected_grpah(n, p)
weights = init_random_weights(adjacency)

print 'Adjacency list:  ' + str(adjacency)
print 'Weights: ' + str(weights)

skeleton = build_minimum_spanning_tree(vertices, weights, dss)
print 'Minimum spanning tree: ' + str(skeleton)

draw_graph(n, adjacency, title='Connected graph', skeleton=skeleton)
