import sys
import math



def diff(ns,i1,i2,i3,i4):
    d = math.fabs((ns[i2]-ns[i1]))*(i4-i3) - (i2-i1)*math.fabs((ns[i4]-ns[i3]))
    return d

# include both start and end
def find(ns,start,end):
    m_i1 = start
    m_i2 = start+1
    if start == end-1:
        return (m_i1,m_i2)
    for i in xrange(start+2,end+1):
        d = diff(ns,start,m_i2,start,i)
        if d < 0:
            m_i2 = i
    if start+1<m_i2:
        (i1,i2) = find(ns,start+1,m_i2)
        d = diff(ns,m_i1,m_i2,i1,i2)
        if d < 0:
            m_i1,m_i2 = i1,i2
    if m_i2+1<end:
        (i1,i2) = find(ns,m_i2+1,end)
        d = diff(ns,m_i1,m_i2,i1,i2)
        if d < 0:
            m_i1,m_i2 = i1,i2
    return (m_i1,m_i2)


def find2(ns,start,end):
    best = start
    for i in xrange(start,end):
        d = diff(ns,best,best+1,i,i+1)
        if d < 0:
            best = i
    return best

n = int(sys.stdin.readline().strip())
ns = [0]
for line in sys.stdin:
    nn = int(line.strip())
    ns.append(nn)

#(i1,i2) = find(ns,1,len(ns)-1)

best = find2(ns,1,len(ns)-1)

print str(best)+' '+str(best+1)
