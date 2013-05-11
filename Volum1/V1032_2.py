import sys
n = int(sys.stdin.readline().strip())

ns = []
b = [0]
m = {}
sum = 0
i = -1
j = 0
for line in sys.stdin:
    nn = int(line.strip())
    ns.append(nn)
    sum += nn
    b.append(sum)
    r = sum % n
    if r == 0:
        j = len(b)-2
        break
    else:
        if not r in m:
            m[r] = []
        m[r].append(len(b)-2)
        if len(m[r])>1:
            i = m[r][0]
            j = m[r][1]
            break

print j-i
for k in xrange(i+1,j+1):
    print ns[k]
            
            


