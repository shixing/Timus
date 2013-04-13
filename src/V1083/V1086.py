import sys
import math

def getSomePrime(start,step,ps):
    results = []
    end = start+step-1
    endsqrt = int(math.sqrt(end))
    array = [0]*step
    for p in ps:
        if p > endsqrt:
            break
        lstart = 0
        for x in xrange(start,start+step):
            if x % p == 0:
                lstart = x
                break
        for x in xrange(lstart-start,step,p):
            array[x] = 1
    for x in xrange(step):
        if array[x] == 0:
            results.append(start+x)
    return results

if __name__== '__main__':

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
    start = 8
    step = ps[-1]*ps[-1]-start
    while True:
        if len(ps) > maxn:
            break
        moreps = getSomePrime(start,step,ps)
        #print len(moreps),moreps
        ps += moreps
        start = start + step
        step = ps[-1]*ps[-1]-start
        if maxn<step:
            step = maxn
    
    for i in na:
        print ps[i-1]




