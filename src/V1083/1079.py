import sys

ns = {}
na = []
maxn = 0
while True:
    line = sys.stdin.readline().strip()
    n = int(line)
    if n == 0:
        break
    ns[n] = 0
    na.append(n)
    if maxn<n:
        maxn = n

a = [0,1]
max = 0
ns[1]=1
for i in xrange(2,maxn+1):
    aa = 0
    if i % 2 == 0:
        aa = a[i/2]
    else:
        aa = a[i/2]+a[i/2+1]
    a.append(aa)
    if max < aa:
        max = aa
    if i in ns:
        ns[i] = max
   

for i in xrange(len(na)):
    print ns[na[i]]
