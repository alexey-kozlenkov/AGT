__author__ = 'alexey'
import algorithms.approximate.set_cover as set_cover
import data

# Override 'get_elements' due to that key in my weighted subset is no subset exactly.
set_cover.get_elements = lambda subset: subset[1]

cover = set_cover.build_set_cover(data.cities, data.weighted_subsets)
print map(lambda x: x[0], cover)
