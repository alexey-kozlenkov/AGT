__author__ = 'Alexey'
import sys


def get_elements(subset):
    return subset


def __get_most_appropriate_subset(weighted_subsets, cover):
    cost = float('inf')
    best_subset = None
    for subset, weight in weighted_subsets.items():
        elements = set(get_elements(subset))
        new_covered_size = len(elements.difference(cover))
        current_cost = weight / new_covered_size if new_covered_size else float('inf')
        if current_cost < cost:
            cost = current_cost
            best_subset = subset
    return best_subset


def __check_subsets(original_set, subsets):
    union = set()
    for subset in subsets:
        elements = get_elements(subset)
        union = union.union(elements)
    if original_set - union:
        print ('Subsets union is not original set.', sys.stderr)
        sys.exit(1)


def build_set_cover(original_set, weighted_subsets):
    elements_cover = set()
    cover = set()
    __check_subsets(original_set, weighted_subsets.keys())
    while elements_cover != original_set:
        best_subset = __get_most_appropriate_subset(weighted_subsets, elements_cover)
        elements_cover.update(get_elements(best_subset))
        cover.add(best_subset)
    return cover
