__author__ = 'Alexey'
import graph_tools.common_utils as utils


def get_simple_vertex_cover(adjacency_param):
    """
    :type adjacency_param: dict
    :return: list of vertices which form a vertex cover.
    """
    adjacency = adjacency_param.copy()
    vertex_cover = []
    size, max_vertex = utils.get_max_vertex(adjacency)
    while size > 0:
        vertex_cover.append(max_vertex)
        utils.remove_vertex(max_vertex, adjacency)
        size, max_vertex = utils.get_max_vertex(adjacency)
    return sorted(vertex_cover)


def depth_first_search(start, target, adjacency, path, labels=None):
    """
    Looks for a path from start vertex to target vertex, using adjacency list
    :type adjacency: dict
    :type path: list
    :return: list of vertices which makes a path.
    """
    if not labels:
        labels = {vertex: False for vertex in adjacency.keys()}

    path.append(start)
    labels[start] = True

    if start == target:
        return True
    for vertex in adjacency[start]:
        if not labels[vertex]:
            if vertex == target:
                path.append(vertex)
                return True
            else:
                result = depth_first_search(vertex, target, adjacency, path, labels)
                if result:
                    return True
    path.pop()
    return False


def check_connectivity(vertices, adjacency):
    vertex = vertices[0]
    labels = {vertex: False for vertex in adjacency.keys()}
    depth_first_search(vertex, None, adjacency, [], labels=labels)
    for vertex in vertices:
        if vertex not in labels or not labels[vertex]:
            return False
    return True


def build_minimum_spanning_tree(vertices, weights, dss):
    """
    Implementation of the Kruskal's algorithm of building minimum spanning tree
    :param vertices:
    :param weights:
    :param dss:
    :return:
    """
    edges = sorted(weights, key=weights.get)
    result = []
    dss.init_data(vertices)
    while dss.sets_count > 1:
        v, u = edges.pop(0)
        if dss.get_root(v) != dss.get_root(u):
            result.append((v, u))
            dss.unite(v, u)
    return result
