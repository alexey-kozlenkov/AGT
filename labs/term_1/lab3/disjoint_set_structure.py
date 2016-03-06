__author__ = 'Alexey'

vertices = []
roots = {}
heights = {}
sets_count = 0


def init_data(vertices_param):
    global vertices, roots, heights, sets_count
    vertices = vertices_param
    roots = {vertex: None for vertex in vertices}
    heights = {vertex: 0 for vertex in vertices}
    sets_count = len(vertices_param)


def insert(vertex):
    global sets_count
    vertices.append(vertex)
    roots[vertex] = None
    heights[vertex] = 0
    sets_count += 1


def get_root(vertex):
    trace = []
    while roots[vertex] is not None:
        trace.append(vertex)
        vertex = roots[vertex]

    for trace_point in trace:
        roots[trace_point] = vertex
    return vertex


def unite(x, y):
    global sets_count
    root_x = get_root(x)
    root_y = get_root(y)
    if root_x == root_y:
        return
    sets_count -= 1

    if heights[root_x] < heights[root_y]:
        roots[root_x] = root_y
        heights[root_x] = 0
    elif heights[root_y] < heights[root_x]:
        roots[root_y] = root_x
        heights[root_y] = 0
    else:
        roots[root_x] = root_y
        heights[root_y] += 1
        heights[root_x] = 0
