import sys

n1 = int(sys.stdin.readline().strip())
n1s = []
for i in xrange(n1):
    n = int(sys.stdin.readline().strip())
    n1s.append(10000-n)
n2 = int(sys.stdin.readline().strip())
n2s = []

for i in xrange(n2):
    n = int(sys.stdin.readline().strip())
    n2s.append(n)

n2s = set(n2s)

answer = 'NO'

for x in n1s:
    if x in n2s:
        answer = 'YES'
        break

print answer
