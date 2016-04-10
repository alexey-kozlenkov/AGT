from graph_tools.graph_drawer import draw_graph

__author__ = 'Alexey'
from copy import deepcopy
from random import uniform

from algorithms.algorithms import build_minimum_spanning_tree
from graph_tools.common_graph_utils import remove_vertex, init_random_weights
from graph_tools.graph_builder import build_random_graph
import algorithms.disjoint_set_structure as dss

n = 10

original_vertices, original_adjacency = build_random_graph(n, 1)

vertices = filter(lambda x: uniform(0, 1) < 0.5, original_vertices)
adjacency = deepcopy(original_adjacency)
difference = set(original_vertices).difference(vertices)
for removed_vertex in difference:
    adjacency = remove_vertex(removed_vertex, adjacency)

weights = init_random_weights(adjacency, limit=10)
spanning_tree = build_minimum_spanning_tree(vertices, weights, dss)

for empty_vertex in difference:
    adjacency[empty_vertex] = []
draw_graph(adjacency, 1, 'Steiner tree', labels=difference, label_color='gray', skeleton=spanning_tree)

for edge in sorted(weights, key=weights.get):
    print str(edge) + ': ', str(weights[edge]) + '; ',
