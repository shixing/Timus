import sys
from collections import deque

class Board:
    def __init__(self,n):
        self.n = n
    
    @staticmethod
    def convert2n(list):
        r = 0
        for s in list:
            for c in s:
                r = r<<1
                if c == 'b':
                    r += 1
        return r
    @staticmethod    
    def win(n):
        if n ==0 or n == (1<<16)-1:
            return True
        else:
            return False
    
    @staticmethod
    def flip(n,i):
        # 0<= i <= 15
        tmp = [i]
        if (i-1)/4 == i/4:
            tmp.append(i-1)
        if (i+1)/4 == i/4:
            tmp.append(i+1)
        if (i+4)<=15:
            tmp.append(i+4)
        if (i-4)>=0:
            tmp.append(i-4)
        nn = n
        #print tmp
        for t in tmp:
            nn = nn ^ (1<<t)
        return nn
    
l = []    
for line in sys.stdin:
    l.append(line.strip())

seen = {}
queue = deque()
success = False

nn = Board.convert2n(l)
queue.append((nn,0))



while len(queue)!=0:
    (n,nstops) = queue.popleft()
    if Board.win(n):
        print nstops
        success = True
        break
    seen[n] = 2
    for p in xrange(0,16):
        nn = Board.flip(n,p)
        if not nn in seen:
            seen[nn] = 1
            queue.append((nn,nstops+1))
            
if not success:
    print 'Impossible'


