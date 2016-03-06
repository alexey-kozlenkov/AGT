__author__ = 'Alexey'
from random import shuffle, randint
import copy


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


def remove_vertex(vertex, adjacency_param):
    """
    :type adjacency_param: dict
    """
    adjacency = copy.deepcopy(adjacency_param)
    adjacency_list = adjacency.get(vertex)
    for adjacent_vertex in adjacency_list:
        adjacency[adjacent_vertex].remove(vertex)
    adjacency.pop(vertex)
    return adjacency

def remove_vertex_with_surrounding(vertex, adjacency_param):
    adjacency = copy.deepcopy(adjacency_param)
    for vertex_to_remove in [vertex] + adjacency[vertex]:
        adjacency = remove_vertex(vertex_to_remove, adjacency)
    return adjacency


def get_min_vertex(adjacency):
    sorted_keys = sorted(adjacency, key=lambda el: len(adjacency[el]))
    return sorted_keys[0]


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
