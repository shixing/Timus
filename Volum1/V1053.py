import sys

n = int(sys.stdin.readline().strip())
ns = []
for line in sys.stdin:
    ns.append(int(line.strip()))

nl = 0
while True:
    
    if len(ns) == 1:
        nl = ns[0]
        break
    m = min(ns)
    if m == 1:
        nl = 1
        break
    mc = sys.maxint
    for x in ns:
        if x == m:
            continue
        shang = int(x/m)
        if shang < mc:
            mc = shang
    
    temp = [m]
    for x in ns:
        t = x-mc*m
        if t>0:
            temp.append(t)
    ns = temp

print nl
