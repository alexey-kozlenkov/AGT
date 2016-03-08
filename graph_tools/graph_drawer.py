__author__ = 'Alexey'
from math import sin, cos, pi

from matplotlib import pyplot as plot


def init_points(n):
    points = {}
    for i in range(n):
        alpha = 2 * pi * float(i) / n
        x = cos(alpha)
        y = sin(alpha)
        points[i + 1] = (x, y)
    return points


def init_canvas(plotter, title, n, p):
    fig = plotter.figure(figsize=(7.5, 7.5), dpi=80)
    ax = fig.add_subplot(111)
    plotter.xlim([-1.3, 1.3])
    plotter.ylim([-1.3, 1.3])
    plotter.axis('off')
    plotter.title(title if title else 'Graph on ' + str(n) + ' vertices')
    props = dict(boxstyle='round', facecolor='white')
    plotter.text(-1.5, 1, 'Random graph\nn = %d\np = %.2f' % (n, p), bbox=props)
    plotter.xkcd()
    return ax


def get_label_color(vertex, labels, label_color):
    return label_color if labels and vertex in labels else 'black'


def get_line_style(v, u, skeleton):
    if skeleton is not None:
        if (v, u) in skeleton or (u, v) in skeleton:
            return 3, 'black'
    return 1.5, 'blue'


def draw_graph(adjacency_list, p, title=None, filename='graph', labels=None, label_color='red', skeleton=None):
    n = len(adjacency_list)
    points = init_points(n)
    ax = init_canvas(plot, title, n, p)

    for vertex in adjacency_list.keys():
        adjacency = adjacency_list.get(vertex)
        coordinates = points.get(vertex)

        mfc = get_label_color(vertex, labels, label_color)
        plot.plot(coordinates[0], coordinates[1], marker='o', mfc=mfc, markersize=12, zorder=3)
        ax.text(coordinates[0] * 1.15, coordinates[1] * 1.15, str(vertex))

        for adjacent_vertex in adjacency:
            vertex_coordinates = points.get(adjacent_vertex)
            line_width, color = get_line_style(vertex, adjacent_vertex, skeleton)
            plot.plot([coordinates[0], vertex_coordinates[0]], [coordinates[1], vertex_coordinates[1]], lw=line_width,
                      color=color)

    plot.savefig(filename + '.png')
