import random

f = open('t.txt','w')

m = 100
n = 500

f.write(str(m)+' '+str(n)+'\n')

for i in xrange(m):
    for j in xrange(n):
        f.write(str(random.randint(0,1000000))+' ')
    f.write('\n')
