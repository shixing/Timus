import sys
import math

def addMorePrime(ps):
    n = ps[-1]+1
    while True:
        nsqrt = int(math.sqrt(n))
        pi = 0
        while True:
            if ps[pi] > nsqrt:
                ps.append(n)
                return
            if n % ps[pi] == 0:
                break
            pi += 1
        n += 1

def factorize(n,ps,m):

    pi = 0

    while True:
        if pi >= len(ps):
            addMorePrime(ps)
        if ps[pi]>n:
            break
        po = 0
        while n % ps[pi] == 0:
            n = n/ps[pi]
            po += 1
        if po != 0:
            if not ps[pi] in m:
                m[ps[pi]] = 0
            m[ps[pi]] += po
        pi += 1
     


ns = []

for line in sys.stdin:
    n = int(line.strip())
    ns.append(n)

ps = [2,3,5,7,11]

m = {}

for n in ns:
    if n == 1:
        continue
    factorize(n,ps,m)

sum = 1

for key in m:
    sum *= (m[key]+1)

print sum % 10
    

