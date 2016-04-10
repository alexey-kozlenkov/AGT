__author__ = 'alexey'

cities = {'red', 'black', 'blue', 'green', 'yellow', 'turquoise', 'orange', 'purple', 'white'}
weighted_subsets = {('red', ('red', 'black', 'blue')): 1.,
                    ('black', ('green', 'black', 'blue', 'green')): 1.,
                    ('blue', ('green', 'black', 'blue', 'green')): 1.,
                    ('green', ('black', 'blue', 'green')): 1.,
                    ('yellow', ('yellow', 'turquoise')): 1.,
                    ('turquoise', ('yellow', 'turquoise')): 1.,
                    ('orange', ('turquoise', 'orange', 'purple')): 1.,
                    ('purple', ('orange', 'purple')): 1.,
                    ('white', ('white',)): 1.}
