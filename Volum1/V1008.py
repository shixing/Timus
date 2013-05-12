import sys
from collections import deque

def A2B(n):
    rl = None
    m = [[0]*12 for x in xrange(11)]

    for line in sys.stdin:
        if not line:
            break
        ll = line.split()
        x = int(ll[0])
        y = int(ll[1])
        if rl == None:
            rl = (x,y)
        m[y][x] = 1

    print rl[0],rl[1]
    # BFS
    queue = deque([])
    queue.append(rl)
    while len(queue)!=0:
        (x,y) = queue.popleft()
        m[y][x] = 2
        # right
        if m[y][x+1] == 1:
            sys.stdout.write('R')
            queue.append((x+1,y))
            m[y][x+1] = 2
        # top
        if m[y+1][x] == 1:
            sys.stdout.write('T')
            queue.append((x,y+1))
            m[y+1][x] = 2
        # left
        if m[y][x-1] == 1:
            sys.stdout.write('L')
            queue.append((x-1,y))
            m[y][x-1] = 2
        # below
        if m[y-1][x] == 1:
            sys.stdout.write('B')
            queue.append((x,y-1))
            m[y-1][x] = 2
        if len(queue) == 0:
            print '.'
        else:
            print ','


def B2A(rl):
    m = [[0]*12 for i in xrange(12)]
    npoints = 0
    queue = deque()
    queue.append(rl)
    
    while len(queue)!=0:
        (x,y) = queue.popleft()
        line = sys.stdin.readline()
        m[y][x] = 1
        npoints += 1
        for c in line:
            if c == 'R':
                queue.append((x+1,y))
            elif c == 'T':
                queue.append((x,y+1))
            elif c == 'L':
                queue.append((x-1,y))
            elif c == 'B':
                queue.append((x,y-1))

    print npoints
    for x in xrange(0,12):
        for y in xrange(0,12):
            if m[y][x] == 1:
                print x,y






line = sys.stdin.readline().strip()

if ' ' in line:
    ll = line.split()
    x = int(ll[0])
    y = int(ll[1])
    B2A((x,y))
else:
    n = int(line)
    A2B(n)
