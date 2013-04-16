import sys

input = sys.stdin

n = int(input.readline().strip())

result = ''

if n == 0:
    print 10
elif n == 1:
    print 1
else:
    while True:
        good = False
        for d in range(9,1,-1):

            if n % d == 0:
                result = str(d)+result
                n = n/d
                good = True
                break

        if n == 1:
            print result
            break
        if not good:
            print -1
            break
