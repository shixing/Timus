import sys
import math
sum = int(sys.stdin.readline().strip())

ns = [-1]*(sum+1)
sqrt = int(math.sqrt(sum))
sqares = [x*x for x in xrange(1,sqrt+1)]
ns[0] = 0

#1
for s in sqares:
    ns[s] = 1
#2
for s1 in sqares:
    for s2 in sqares:
        if s1+s2 >= len(ns):
            continue
        if ns[s1+s2] == -1:
            ns[s1+s2]=2
#3

for s1 in sqares:
    for s2 in sqares:
        for s3 in sqares:
            if s1+s2+s3 >= len(ns):
                continue
            if ns[s1+s2+s3] == -1:
                ns[s1+s2+s3]=3



def cal(n):
    if ns[n] != -1:
        return ns[n]
    min = sys.maxint
    x = int(math.sqrt(n))
    while True:
        xx = x*x
        x-=1
        if xx==0:
            break
        temp = cal(n-xx)+1
        if min > temp:
            min = temp
    ns[n] = min
    return min


print cal(sum)

