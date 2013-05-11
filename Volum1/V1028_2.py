import sys

class BIT:
    def __init__(self,length):
        self.tree = [0]*(length+1)
        self.length = length

    def update(self,x,add):
        while x<=self.length:
            self.tree[x] += add
            x += (x & -x)

    # not tree(idx)-tree(idx-1) but some quicker thing
    def get(self,i):
        if i > 0:
            sum = self.tree[i]
            z = i - (i & -i)
            i-=1
            while i != z:
                sum -= self.tree[i]
                i -= (i & -i)
            return sum
        else:
            return 0
        
    def getCum(self,i):
        sum = 0
        while i>0:
            sum += self.tree[i]
            i -= (i & -i)
        return sum

    def printAll(self):
        temp = []
        for i in xrange(1,self.length+1):
            temp.append( self.get(i) )
        print temp


def main():
    n = int(sys.stdin.readline().strip())
    bit = BIT(32010)
    levels = [0]*n
    for line in sys.stdin:
        ll = line.split()
        x = int(ll[0])+1
        bit.update(x,1)
        level = bit.getCum(x) - 1
        levels[level] +=1
    
    
    for l in levels:
        print l

if __name__ == '__main__':
    main()
