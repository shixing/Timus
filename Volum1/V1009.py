import sys

input = sys.stdin

n = input.readline().strip()
n = int(n)
k = input.readline().strip()
k = int(k)

m = [[0]*n,[0]*n]
m[1][0]=k-1

for i in xrange(1,n):
    m[0][i]=m[1][i-1]
    m[1][i]=(m[0][i-1]+m[1][i-1])*(k-1)

print m[0][n-1]+m[1][n-1]
