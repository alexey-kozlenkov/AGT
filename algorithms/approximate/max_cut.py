from graph_tools.bipartite_utils import simple_divide_vertices, extract_bipartite_adjacency, move_vertex

__author__ = 'Alexey'


def build_max_cut(adjacency):
    left, right = simple_divide_vertices(adjacency.keys())
    bipartite_adjacency = extract_bipartite_adjacency(adjacency, left, right)
    v = find_vertex(adjacency, bipartite_adjacency)
    while v:
        left, right = move_vertex(v, left, right)
        bipartite_adjacency = extract_bipartite_adjacency(adjacency, left, right)
        v = find_vertex(adjacency, bipartite_adjacency)
    return bipartite_adjacency, left, right


def find_vertex(adjacency, bipartite_adjacency):
    for v in adjacency.keys():
        if len(adjacency[v]) > 2 * len(bipartite_adjacency[v]):
            return v
    return None
