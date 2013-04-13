import sys
import math
input = sys.stdin

line = input.readline().strip().split()

n = int(line[0])
r = float(line[1])
ords = []
while True:
    line = input.readline()
    if not line:
        break
    ll = line.split()
    ord = (float(ll[0]),float(ll[1]))
    ords.append(ord)

sum = 0
for i in xrange(n):
    i1 = i
    i2 = (i + 1) % n
    sum += math.sqrt( math.pow(ords[i1][0]-ords[i2][0],2) + math.pow(ords[i1][1]-ords[i2][1],2) )

sum += 2*3.141592653*r

print '%.2f' % sum
