import sys

n = int(sys.stdin.readline().strip())

m = [[0]*n for x in xrange(n)]

i = 0

for line in sys.stdin:
    j=0
    for c in line.strip():
        if c == '#':
            m[i][j] = -1
        j += 1
    i +=1


# wall -1
# white 0
# gray 1
# black 2
def getNeighbours(xy):
    candidates = []
    offset0 = [0,0,1,-1]
    offset1 = [-1,1,0,0]
    sum = 0
    for i in xrange(4):
        x = xy[0]+offset0[i]
        y = xy[1]+offset1[i]
        if x>=0 and x<n and y>=0 and y<n:
            if m[x][y] == 0:
                candidates.append((x,y))
            elif m[x][y] == -1:
                sum += 1
        else:
            sum += 1
    return (candidates,sum)


# bfs

def bfs(initxy,sum):
    queue = []
    queue.append( initxy )

    while len(queue) !=0:
        xy = queue[0]
        del queue[0]
        m[ xy[0] ][ xy[1] ] = 2 #black
        (neightbours,s) = getNeighbours(xy)
        #print xy , neightbours,s
        sum += s
        for nxy in neightbours:
            m[ nxy[0] ][ nxy[1] ] = 1
            queue.append(nxy)
    
    return sum

sum = 0
sum += bfs((0,0),sum)

# for row in m:
#     print row

if m[n-1][n-1] != 2:
    sum = bfs((n-1,n-1),sum)

# for row in m:
#     print row

print (sum-4)*9
