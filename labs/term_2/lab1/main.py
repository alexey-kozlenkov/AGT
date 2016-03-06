__author__ = 'Alexey'
from graph_tools.graph_builder import build_random_graph
from graph_tools.graph_drawer import draw_graph
from algorithms.algorithms import find_maximum_independent_set


vertices, adjacency = build_random_graph(10, 0.5)
draw_graph(10, adjacency, filename='Start graph')
print(find_maximum_independent_set(adjacency))
