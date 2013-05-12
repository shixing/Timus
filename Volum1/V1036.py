import sys

line = sys.stdin.readline().split()
n = int(line[0])
s = int(line[1])

m = [{} for x in xrange(n+1)]

def f(i,sum):
    
    if sum==0:
        return 1
    if sum<0 or i==0:
        return 0
    
    if sum in m[i]:
        return m[i][sum]
    t = 0
    for x in xrange(0,min(10,sum+1)):
        t += f(i-1,sum-x)
    m[i][sum]=t
    return t


if s%2 !=0:
    print 0
else:
    s = s/2
    r = f(n,s)
    print r*r
    
