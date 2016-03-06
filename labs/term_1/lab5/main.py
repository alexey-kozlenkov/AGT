__author__ = 'Alexey'
from graph_tools.bipartite_utils import build_maximum_matching

log = open("input.txt")
left, right = [], []
left += log.readline().strip().split(' ')
right += log.readline().strip().split(' ')
edges = []

line = log.readline()
while len(line) > 0:
    card, cover = map(int, line.strip().split(' '))
    edges.append((left[card - 1], right[cover - 1]))
    line = log.readline()

max_matching = build_maximum_matching(left, right, edges)
print 'Maximum matching: ' + str(max_matching)

print 'Next matches are most rational:'
for match in max_matching:
    print '\t Send ' + match[0] + ' with ' + match[1] + ';'
