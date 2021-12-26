from ssearch_for import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']


print(seq_search(t, 5.6))
print(seq_search(s, 'r'))
print(seq_search(a, 'AAC'))