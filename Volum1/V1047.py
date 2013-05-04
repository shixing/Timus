import sys

n = int(sys.stdin.readline().strip())

a_0 = float(sys.stdin.readline().strip())
a_np1 = float(sys.stdin.readline().strip())

c = [0]
for line in sys.stdin:
    cc = float(line.strip())
    c.append(cc)

m={}
m[0] = a_0
m[n+1] = a_np1

sum = 0
for i in xrange(1,n+1):
    sum += (n+1-i)*c[i]
f = (m[n+1]-m[0] - 2*sum)/(n+1) + m[0]

print '%.2f' % f
