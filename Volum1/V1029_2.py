import sys


line = sys.stdin.readline().split()
m = int(line[0])
n = int(line[1])

floor = [[0]*n for x in xrange(m)]
father = [[None]*n for x in xrange(m)]

ni = 0
for line in sys.stdin:
   ll = line.split()
   for i in xrange(len(ll)):
       floor[ni][i] = int(ll[i])
   ni+=1




max_int = sys.maxint
min_fee = floor[0]
next_min_fee =  [-1]*n 

f = 1

while f<m:
    for i in xrange(n):
        next_min_fee[i] = min_fee[i]+floor[f][i]
        father[f][i] = (f-1,i)
    for i in xrange(n-1):
        if next_min_fee[i]+floor[f][i+1] < next_min_fee[i+1]:
            next_min_fee[i+1] = next_min_fee[i]+floor[f][i+1]
            father[f][i+1] = (f,i)
    for i in xrange(n-1,0,-1):
        if next_min_fee[i]+floor[f][i-1] < next_min_fee[i-1]:
            next_min_fee[i-1] = next_min_fee[i]+floor[f][i-1]
            father[f][i-1] = (f,i)
    min_fee = next_min_fee
    next_min_fee =  [-1]*n 
    f += 1

#print father

best_j = 0
min_value = sys.maxint
for i in xrange(n):
    if min_value > min_fee[i]:
        min_value = min_fee[i]
        best_j = i

results = []

cor = (m-1,best_j)
f = father[m-1][best_j]
results.append(best_j+1)

while f!=None:
    cor = f
    results.append(cor[1]+1)
    f = father[cor[0]][cor[1]]


print ' '.join([str(x) for x in reversed(results)])
