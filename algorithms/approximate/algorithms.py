__author__ = 'Alexey'
from graph_tools.common_graph_utils import remove_vertex


def vertex_cover(adjacency):
    """
    :type adjacency: dict
    """
    result = []
    while adjacency:
        v = adjacency.keys()[0]
        if adjacency[v]:
            u = adjacency[v][0]

            result.append(u)
            result.append(v)

            adjacency = remove_vertex(v, adjacency)
            adjacency = remove_vertex(u, adjacency)
        else:
            adjacency.pop(v)
    return result

