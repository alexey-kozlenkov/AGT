from algorithms.algorithms import check_connectivity

__author__ = 'Alexey'
import random


def init_vertices(n):
    return [i + 1 for i in range(n)]


def init_random_graph(n, p, vertices):
    adjacency = {vertices[i]: [] for i in range(n)}
    for i in range(n):
        v = vertices[i]
        for j in range(i + 1, n):
            u = vertices[j]
            if flip_coin(p):
                create_edge(v, u, adjacency)
    return adjacency


def create_edge(v, u, adjacency):
    adjacency[v].append(u)
    adjacency[u].append(v)


def flip_coin(p):
    coin = random.uniform(0, 1)
    return coin - p < 0


def build_random_graph(n, p):
    vertices = init_vertices(n)
    adjacency = init_random_graph(n, p, vertices)
    yield vertices
    yield adjacency


def build_connected_grpah(n, p):
    vertices = init_vertices(n)
    adjacency = init_random_graph(n, p, vertices)
    while not check_connectivity(vertices, adjacency):
        print ('Rebuild graph due to its disconnection.')
        vertices = init_vertices(n)
        adjacency = init_random_graph(n, p, vertices)
    yield vertices
    yield adjacency
