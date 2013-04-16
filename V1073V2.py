import sys
import math
sum = int(sys.stdin.readline().strip())

ns = [-1]*(sum+1)
sqrt = int(math.sqrt(sum))
sqares = [x*x for x in xrange(1,sqrt+1)]
ns[0] = 0

n =sum

def isSquare(n):
    if int(math.sqrt(n))*int(math.sqrt(n)) == n:
        return True
    else:
        return False
def main():
    if n == 0:
        print 0
        return
    if isSquare(n):
        print 1
        return
    for s1 in sqares:
        if isSquare(n-s1):
            print 2
            return
    for s1 in sqares:
        for s2 in sqares:
            if s1+s2>n:
                break
            if isSquare(n-s1-s2):
                print 3
                return
    print 4

main()
