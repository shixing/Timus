import sys
from collections import deque
n = int(sys.stdin.readline().strip())

ns = [set() for x in xrange(n+1)]

i = 1
for line in sys.stdin:
    ll = [int(x) for x in line.split()[:-1]]
    for l in ll:
        ns[i].add(l)
        ns[l].add(i)
    i+=1

color = [2]*(n+1)
color[1] = 0

queue = deque([1])

fail = 0
while len(queue)!=0:
    a =queue.popleft()
    cc = color[a]
    for neigh in ns[a]:
        if color[neigh] == 2:
            color[neigh] = 1-cc
            queue.append(neigh)
        elif color[neigh] == cc:
            fail = 1
            break
    if fail == 1:
        break

if fail == 1:
    print -1
else:
    print ''.join([str(x) for x in color[1:]])
