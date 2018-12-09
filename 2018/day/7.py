from networkx import DiGraph, lexicographical_topological_sort as lt_sort

data = [(i[1], i[-3]) for i in map(str.split, open('../input/7.txt').readlines())]
print(''.join(lt_sort(DiGraph(data))))

step_reqs = {i: set() for i in (j for i in data for j in i)}
for i in data:
    step_reqs[i[1]].add(i[0])

cnt, d = 0, {}
while step_reqs:
    [0 for i in list(step_reqs.keys()) if not step_reqs[i] and (d.update({i: cnt + ord(i) - 4}) or step_reqs.pop(i))]
    cnt += 1
    [0 for c in d for c2 in step_reqs if d[c] == cnt and c in step_reqs[c2] and step_reqs[c2].remove(c)]

# prints shortest path i.e. as if there were infinite number of workers rather than 5 as in the task
print max(d.values())
