import sys
import math

def gcd(a,b):
    a0 = a
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    if a0<0:
        return - int(math.fabs(b))
    else:
        return int(math.fabs(b))

def genABC(p1,p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    if a == 0:
        c = - b*(p1[1])
        if c == 0:
            return (0,1,0)
        else:
            g = gcd(b,c)
            return (0,b/g,c/g)
    elif b== 0:
        c = - a * p1[0]
        if c == 0:
            return (1,0,0)
        else:
            g = gcd(a,c)
            return (a/g,0,c/g)
    else:
        c = - b*p1[1] - a * p1[0] 
        g1 = gcd(a,b)
        if c == 0:
            return (a/g1,b/g1,0)
        else:
            g = gcd(g1,c)
            return (a/g,b/g,c/g)


n = int(sys.stdin.readline().strip())
points = []

for i in xrange(n):
    line = sys.stdin.readline()
    ll = line.split()
    points.append( (int(ll[0]),int(ll[1])) )

tmax = 0

for i in xrange(len(points)):
    map = {}
    max = 0
    for j in xrange(i+1,len(points)):
        abc = genABC(points[i],points[j])
        if not abc in map:
            map[abc] = 1
        m = map[abc]
        m += 1
        map[abc] = m
        if max<m:
            max = m

    if tmax < max:
        tmax = max


print tmax
