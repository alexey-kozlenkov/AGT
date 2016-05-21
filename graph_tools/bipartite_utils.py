from graph_tools.graph_builder import create_edge

__author__ = 'Alexey'
from algorithms.algorithms import depth_first_search

left_part = []
right_part = []
edges = []


def init_data(left, right, edges_param):
    global left_part, right_part, edges
    edges = edges_param
    left_part = left
    right_part = right


def get_edges_from_vertex_path(path):
    result = []
    previous = path[0]
    for vertex in path[1:]:
        result.append((previous, vertex))
        previous = vertex
    return result


def order_edges(shuffled_edges):
    """
    Rob edges of their orientation, i.e. order edges form the left part to the right part.
    :param shuffled_edges: edges to reorder.
    :type shuffled_edges: list
    :return: ordered edges
    """
    ordered_edges = []
    for edge in shuffled_edges:
        if edge[0] in left_part and edge[1] in right_part:
            ordered_edges.append(edge)
        else:
            ordered_edges.append(edge[::-1])
    return ordered_edges


def orient_graph_by_matching(matching):
    """
        This method has a double-function:

        1) based on matching list, it build oriented adjacency list
        (if edge in matching - an orientation goes from the right part into the left, else - backward)

        2) all vertices from the left part, which are not in matching,
        get one more incoming edge from a spurious vertex 'start', and all vertices from the right part
        get one more outcoming edge into a spurious vertex 'finish'. Finish and Start vertex
        will be used by a DFS algorithm later.
    :param matching: current graph matching
    :return: oriented adjacency list with 'start' and 'finish' vertices.
    """
    starts = list(left_part)
    finishes = list(right_part)
    oriented_adjacency = {}
    oriented_adjacency.update({vertex: [] for vertex in left_part})
    oriented_adjacency.update({vertex: [] for vertex in right_part})

    for edge in edges:
        card, cover = edge
        if edge in matching:
            starts.remove(card)
            finishes.remove(cover)
            oriented_adjacency[cover].append(card)
        else:
            oriented_adjacency[card].append(cover)
    oriented_adjacency['start'] = starts
    oriented_adjacency['finish'] = []
    for finish in finishes:
        oriented_adjacency[finish].append('finish')

    return oriented_adjacency


def make_symmetric_difference(first, second):
    """
    Makes symmetric difference of two storages.
    """
    for element in first:
        if element in second:
            first.remove(element)
            second.remove(element)
    first.extend(second)
    return first


def find_augmenting_chain(matching):
    """
    Finds an augmenting chain for current matching, if it exist, using DFS from start into finish vertices.

    A Start vertex is a vertex with outcoming edges into all no-matched vertices in the left part,

    and a Finish vertex is a vertex with incoming edges from all no-matched vertices from the right part.

    :param matching: current graph matching
    :return: a found chain.
    """
    chain = []
    oriented_adjacency = orient_graph_by_matching(matching)
    depth_first_search('start', 'finish', oriented_adjacency, path=chain)
    return chain


def rebuild_matching(matching, chain):
    """
    Quite simple method which updates current matching to a better version, using found augmented chain.

    :param matching: current matching
    :param chain: augmented chain for :matching
    :return: a better matching
    """
    chain = get_edges_from_vertex_path(chain[1:len(chain) - 1])
    chain = order_edges(chain)
    matching = make_symmetric_difference(matching, chain)
    return matching


def build_maximum_matching(left, right, edges_param):
    init_data(left, right, edges_param)
    matching = []

    chain = find_augmenting_chain(matching)
    while len(chain) > 0:
        matching = rebuild_matching(matching, chain)
        chain = find_augmenting_chain(matching)
    return matching


def simple_divide_vertices(vertices):
    left = vertices[::2]
    right = vertices[1::2]
    return left, right


def extract_bipartite_adjacency(adjacency, left, right):
    bipartite_adjacency = {v: [] for v in adjacency.keys()}
    for v in left:
        adjacency_list = adjacency[v]
        for u in adjacency_list:
            if u in right:
                create_edge(v, u, bipartite_adjacency)
    return bipartite_adjacency


def move_vertex(v, left, right):
    if v in left:
        left.remove(v)
        right.append(v)
    elif v in right:
        right.remove(v)
        left.append(v)
    return left, right
