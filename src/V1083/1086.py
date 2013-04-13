import sys
import math
n = int(sys.stdin.readline().strip())
ns = {}
na = []
maxn = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    nn = int(line.strip())
    ns[nn]=0
    na.append(nn)
    if maxn < nn:
        maxn =nn

ps = [2,3,5,7]

def isPrime(n):
    nsqrt = int(math.sqrt(n))
    isPrimeB = True
    for p in ps:
        if p>nsqrt:
            break
        if n % p ==0:
            isPrimeB = False
    return isPrimeB


i = 10

while True:
    if len(ps)>=maxn:
        break
    if isPrime(i):
        ps.append(i)
    i+=1
for i in na:
    print ps[i-1]
