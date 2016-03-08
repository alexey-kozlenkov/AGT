__author__ = 'Alexey'
from graph_tools.graph_builder import build_random_graph
from graph_tools.graph_drawer import draw_graph
from algorithms.algorithms import find_maximum_independent_set

n = 10
p = 0.5

vertices, adjacency = build_random_graph(n, p)
print 'Graph: ', adjacency
independence_number, mis = find_maximum_independent_set(adjacency)
print 'Maximum independent set: ', list(mis), ' (alfa = %d)' % len(mis)
draw_graph(n, adjacency, title='Maximum independent set.', filename='graph',  labels=mis)
