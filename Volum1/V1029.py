import sys
from collections import deque


line = sys.stdin.readline().split()
m = int(line[0])
n = int(line[1])

floor = [[0]*n for x in xrange(m)]
min_fee = [[-1]*n for x in xrange(m)]
#heap_pos = [[-1]*n for x in xrange(m)]
#state = [[0]*n for x in xrange(m)]
father = [[None]*n for x in xrange(m)]



ni = 0
for line in sys.stdin:
   ll = line.split()
   for i in xrange(len(ll)):
       floor[ni][i] = int(ll[i])
   ni+=1


class heap:
    def __init__(self,compare):
        self.array = []
        self.tail = 0
        self.func = compare
        #self.heap_pos = heap_pos
    
    def change_pos(self,node,pos):
        self.heap_pos[node[0]][node[1]] = pos

    def add(self,node):
        if self.tail>=len(self.array):
            self.array.append(None)
        self.array[self.tail] = node
        self.tail += 1
        # flow up
        idx= self.tail-1
        father = (idx-1)/2
        while father>=0:
            #if self.func(self.array[father],self.array[idx])>0:
            if (self.array[father][2]-self.array[idx][2])>0:
                self.array[father],self.array[idx] =self.array[idx],self.array[father]
                idx = father
                father = (idx-1)/2
            else:
                break



    def pop(self):
        if len(self.array)>0:
            result = self.array[0]
            self.tail -= 1
            self.array[0] = self.array[self.tail]
            idx = 0
            while idx<self.tail:
                left = 2*idx + 1
                right = 2*idx + 2
                min_id = None
                if right<self.tail:
                    if (self.array[left][2]-self.array[right][2])<=0:
                        min_id = left
                    else:
                        min_id = right
                elif right == self.tail:
                    min_id = left
                elif left >= self.tail:
                    break
                if (self.array[idx][2]-self.array[min_id][2])>0:
                    self.array[idx],self.array[min_id] = self.array[min_id],self.array[idx]
                    idx = min_id
                else:
                    break
        
            return result
        else:
            return None
    
    def peak(self):
        if len(self.array)>0:
            return self.array[0]
        else:
            return None
    def check(self):
        print self.array[:self.tail]

    def size(self):
        return self.tail

    def update(self,node): #the new_value could only be smaller
        pos = self.heap_pos[node[0]][node[1]]
        if pos<0 or pos>=self.tail:
            return
        idx= pos
        father = (idx-1)/2
        while father>=0:
            if self.func(self.array[father],self.array[idx])>0:
                self.array[father],self.array[idx] =self.array[idx],self.array[father]
                self.change_pos(self.array[father],father)
                self.change_pos(self.array[idx],idx)
                idx = father
                father = (idx-1)/2
            else:
                break




def compare(node1,node2):
    return node1[2]-node2[2]

min_fee[0] = floor[0]
#state[0] = [2]*n

h = heap(compare)

for i in xrange(n):
    h.add((0,i,floor[0][i]))

best_j = 0
num = 0
nsize = 0
while h.size()!=0:
    num+=1
    nsize+=h.size()
    (i,j,fee) = h.pop()
    #print i,j,fee
    #state[i][j] = 2
    if i == m-1:
        best_j = j
        break

    buf = [(i,j-1),(i,j+1),(i+1,j)]
    for (x,y) in buf:
        if y>=0 and y<n and x<m:
            if min_fee[x][y] < 0:
                new_fee = fee + floor[x][y]
                min_fee[x][y] = new_fee
                father[x][y] = (i,j)
                h.add((x,y,new_fee))
                    
#print min_fee
#print father
print n*m,num,nsize,nsize/num
results = []

cor = (m-1,best_j)
f = father[m-1][best_j]
results.append(best_j+1)

while f!=None:
    cor = f
    results.append(cor[1]+1)
    f = father[cor[0]][cor[1]]


print ' '.join([str(x) for x in reversed(results)])

