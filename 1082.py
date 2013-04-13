import sys

input = sys.stdin

n = int(input.readline().strip())

array = range(1,n+1)

print ' '.join([str(x) for x in array])
