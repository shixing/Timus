import sys

def gcd(a,b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a%b
    return b

def lcm(a,b):
    return a*b/gcd(a,b)

def lcma(array):
    a = array[0]
    for i in xrange(1,len(array)):
        b = array[i]
        a = lcm(a,b)
    return a

def order(p,id):
    o = 1
    pn = p[id]
    while pn != id:
        pn = p[pn]
        o += 1
    return o

n = int( sys.stdin.readline().strip() )
line = sys.stdin.readline()
ll = line.split()
p = [0]+[int(x) for x in ll]

array = []
for i in xrange(1,n+1):
    array.append(order(p,i))

print lcma(array)

        
