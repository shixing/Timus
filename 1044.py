import sys
import math
n = int(sys.stdin.readline().strip())
n = n/2

m = [{},{},{},{}]

for i in xrange(10):
    m[0][i]=1

for nd in xrange(1,n):
    for sum in xrange(nd*9+9,-1,-1):
        tsum = 0
        for i in xrange(9,-1,-1):
            rest = sum - i
            if rest in m[nd-1]:
                tsum += m[nd-1][rest]
        m[nd][sum] = tsum
#print m

total = 0
for sum in xrange(0,n*9+1):
    total += math.pow(m[n-1][sum],2)

print int(total)
