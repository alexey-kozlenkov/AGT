__author__ = 'Alexey'
from random import shuffle, randint


def sort_graph_adjacency(adjacency):
    """
    :type adjacency: dict
    """
    vertices = adjacency.keys()
    sort_adjacency = {vertex: [] for vertex in vertices}
    for vertex in vertices:
        adjacent_vertices = adjacency[vertex]
        for adjacent_vertex in adjacent_vertices:
            sort_adjacency[adjacent_vertex].append(vertex)
    return sort_adjacency


def shuffle_adjacency(adjacency):
    """
    :type adjacency: dict
    """
    shuffled = adjacency.copy()
    for adjacency_list in shuffled.values():
        shuffle(adjacency_list)
    return shuffled


def remove_vertex(vertex, adjacency):
    """
    :type adjacency: dict
    """
    adjacency_list = adjacency.get(vertex)
    for adjacent_vertex in adjacency_list:
        vertex_adjacency_list = adjacency.get(adjacent_vertex)
        vertex_adjacency_list.remove(vertex)
    adjacency.pop(vertex)


def get_max_vertex(adjacency):
    """
    :type adjacency: dict
    """
    max_size = 0
    max_size_vertex = 0
    for vertex in adjacency.keys():
        adjacency_list = adjacency.get(vertex)
        if len(adjacency_list) > max_size:
            max_size = len(adjacency_list)
            max_size_vertex = vertex
    yield max_size
    yield max_size_vertex


def init_random_weights(adjacency, limit=None):
    if limit is None:
        limit = len(adjacency) * 2
    weights = {}
    for v in adjacency.keys():
        for u in adjacency[v]:
            if (u, v) not in weights and (v, u) not in weights:
                weight = randint(1, limit)
                weights[(v, u)] = weight
    return weights
