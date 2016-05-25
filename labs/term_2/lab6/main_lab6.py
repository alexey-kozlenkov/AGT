__author__ = 'Alexey'
from algorithms.approximate.max_cut import build_max_cut
from graph_tools.common_graph_utils import get_edges
from graph_tools.graph_drawer import draw_graph
from graph_tools.graph_builder import build_random_graph

n = 8
p = 0.5
vertices, adjacency = build_random_graph(n, p)
bipartite_adjacency, left, right = build_max_cut(adjacency)
skeleton = get_edges(bipartite_adjacency)
draw_graph(adjacency, p, 'Max cut', labels=[(left, 'steelblue'), (right, 'orange')], skeleton=skeleton)
