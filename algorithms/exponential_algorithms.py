__author__ = 'Alexey'
import math
from algorithms import dichotomy


def build_characteristic_polynom(t_list):
    t = max(t_list)
    return lambda x: sum([x ** t] + [-x ** (t - t_i) for t_i in t_list])


def format_number(x):
    return math.ceil(x * 10000) / 10000


def calculate_branching_multiplier(t_list):
    p = build_characteristic_polynom(t_list)
    r = len(t_list)
    return format_number(dichotomy(p, 1, r, 10 ** -5))
