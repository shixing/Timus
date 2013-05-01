import sys
import math

n = int(sys.stdin.readline().strip())

sn = int(math.sqrt(n))

l = 0
for i in xrange(3,sn+1):
    if n % i == 0:
        l = i-1
        break
if l == 0:
    if n % 2 == 0:
        l = n/2-1
    else:
        l = n - 1
if n == 4:
    l = 3

print l
    
