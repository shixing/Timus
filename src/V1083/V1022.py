import sys

n = int(sys.stdin.readline().strip())
nfathers = [0]*n
childrens = []
for i in xrange(n):
    line = sys.stdin.readline().split()
    children = [int(x)-1 for x in line][:-1]
    childrens.append(children)
    for x in children:
        nfathers[x]+=1

rank = []

def pushRank(i):
    rank.append(i)
    nfathers[i] = -1
    for c in childrens[i]:
        nfathers[c] -= 1
        if nfathers[c] == 0:
            pushRank(c)
    


while len(rank)<n:
    for i in xrange(n):
        if nfathers[i] == 0:
            pushRank(i)

rank = [str(x+1) for x in rank]

print ' '.join(rank)
