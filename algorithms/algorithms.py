__author__ = 'Alexey'
import graph_tools.common_graph_utils as utils


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


def find_maximum_independent_set(adjacency):
    """
    Computing MIS and independence number for a graph.
    :type adjacency: dict
    """
    if not len(adjacency):
        return 0, set()
    min_vertex = utils.get_min_vertex(adjacency)
    variants = {}
    for v in [min_vertex] + adjacency[min_vertex]:
        independence_number, mis = find_maximum_independent_set(utils.remove_vertex_with_surrounding(v, adjacency))
        mis.add(v)
        variants[independence_number] = mis
    max_independence_number = max(variants.keys())
    return 1 + max_independence_number, variants[max_independence_number]


def dichotomy(func, a, b, eps):
    mid = float(a + b) / 2
    y = func(mid)
    while b - a > eps:
        if y == 0:
            return mid
        elif y < 0:
            return dichotomy(func, mid, b, eps)
        else:
            return dichotomy(func, a, mid, eps)
    return b
