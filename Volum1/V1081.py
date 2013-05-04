import sys

line = sys.stdin.readline().split()
n = int(line[0])
k = int(line[1])


num = [0] * n

def calfab(k):
    if 2 >= k:
        return [2]
    if 3 >= k:
        return [2,3]
    fab = [2,3]
    i = 0
    while True:
        f = fab[i]+fab[i+1]
        fab.append(f)
        i+=1
        if f >= k:
            return fab

def main(n,k):
    fab = calfab(k)
    if len(fab) > n:
        print -1
        return
    #print fab
    rest = k
    for i in xrange(len(fab)-1,-1,-1):
        if rest <= 2:
            break
        if rest > fab[i]:
            num[i+1] = 1
            rest = rest - fab[i]

    if rest == 2:
        num[0] = 1

    num.reverse()
    print ''.join([str(x) for x in num])
    
main(n,k)
