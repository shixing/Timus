import sys
import math

def run2(n):
    maxj = int(math.sqrt(2*n+0.25)-0.5)
    f = [[0]*(n+1) for x in xrange(maxj+1)]
    f[1][1] = 1
    for i in xrange(2,n+1):
        for j in xrange(1, int(math.sqrt(2*i+0.25)-0.5)+1):
            f[j][i] = f[j][i-j] + f[j-1][i-j]
    print sum([x[n] for x in f])-1



def run(n):
# f(n,n-1)

    f = [[-1] * n for x in xrange(n+1)]
    for i in xrange(n):
        f[1][i]=1
    ss=[0,0,n*n+n]
    def calf(n,l,s):
        ss[0]+=1
        if n>0 :
            if f[n][l]!=-1:
                ss[1]+=1
                return f[n][l]
            m = min(n,l)
            sum = 0
            for i in xrange(m,int(math.sqrt(2*n+0.25)-0.5-0.01),-1):
                #if n > i*(i+1)/2:
                #    break
                sum += calf(n-i,i-1,s-1)
            f[n][l] = sum
            return sum
        if n == 0:
            if s>=1:
                return 0
            else:
                return 1
        
    print calf(n,n-1,2)

    print sum([1 for x in f for y in x if y!=-1 ])
    print ss

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    run2(n)
