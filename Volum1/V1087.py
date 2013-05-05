import sys

sys.setrecursionlimit(10050)



def calwin2(n,ks):
    for i in xrange(1,n+1):
        if wins2[i] == 2:
            for k in ks:
                if k+i <= n:
                    wins2[k+i] = 1
    return wins2[n]

def calwin(n,ks):
    if n in wins:
        return wins[n]
    if n<=ks[0]: 
        wins[n] = 2
        return wins[n]

    for k in ks:
        if n - k <= 0:
            break
        w = calwin(n-k,ks)
        if w == 2:
            wins[n] = 1
            return 1
    wins[n] = 2
    return 2

line = sys.stdin.readline().split()
n = int(line[0])
m = int(line[1])


line = sys.stdin.readline().split()
ks = [int(x) for x in line]
ks = sorted(ks)

wins = {}
wins2 = [2]*(n+1)

print calwin2(n,ks)

