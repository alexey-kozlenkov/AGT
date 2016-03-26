from algorithms.approximate.algorithms import vertex_cover
from graph_tools.graph_builder import build_random_graph, build_connected_graph
from graph_tools.graph_drawer import draw_graph

__author__ = 'Alexey'


n = 7
p = 0.3


vertices, adjacency = build_connected_graph(n, p)
approximate_cover = vertex_cover(adjacency)
draw_graph(adjacency, p, title='Approximate vertex cover', labels=approximate_cover)
