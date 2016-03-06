__author__ = 'Alexey'
from graph_tools.graph_builder import build_random_graph
from graph_tools.graph_drawer import draw_graph

n = input("Enter vertices number: ")
p = input("Enter probability: ")

if type(n) != int or type(p) != float:
    print "Your input is invalid, sorry :C Try again?"
    exit(1)

vertices, adjacency = build_random_graph(n, p)
print(adjacency)

draw_graph(n, adjacency, 'Random graph, n=%d, p=%.2f' % (n, p))
