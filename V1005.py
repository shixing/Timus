import sys

input = open('test.txt','r')    
#input = sys.stdin

n = int(input.readline().strip())
nums = input.readline().strip().split()
nums = [int(x) for x in nums]

def mm(m,i,j):
    if j<0 or i<0:
        return -1
    else:
        return m[i][j]

# talbe DP
def tableDP(n,nums):
    total = reduce(lambda x,y:x+y,nums)
    sum = total/2
    m = [[0]*n for x in xrange(sum+1)]
    for i in xrange(sum+1):
        if i>=nums[0]:
            m[i][0]=nums[0]
    for j in xrange(1,n):
        for i in xrange(1,sum+1):
            m1 = mm(m,i-nums[j],j-1)
            m2 = mm(m,i,j-1)
            if m1 < 0:
                m[i][j] = m2
            else:
                m[i][j] = max( m1+nums[j], m2)
    print total-2*m[sum][n-1]
    
# arrayDP
def arrayDP(n,nums):
    total = reduce(lambda x,y:x+y,nums)
    sum = total/2
    m = [0]*(sum+1)
    for i in xrange(sum+1):
        if i >= nums[0]:
            m[i]= nums[0]

    for j in xrange(1,n):
        for i in xrange(sum,0,-1):
            if i-nums[j] >= 0:
                m1 = m[i-nums[j]]+nums[j]
                m[i] = max(m[i],m1)
    print total - 2 * m[sum]


# iterative DP
def iteDP(n,nums):
    total = reduce(lambda x,y:x+y,nums)
    sum = total/2
    m = [[-1]*n for x in xrange(sum+1)]
    for i in xrange(sum+1):
        if i>=nums[0]:
            m[i][0]=nums[0]
        else:
            m[i][0]=0
    for i in xrange(n):
        m[0][i]=0
    def dp(i,j):
        if m[i][j]>=0:
            return m[i][j]
        else:
            m2 = dp(i,j-1)
            if i-nums[j]>=0:
                m1 = dp(i-nums[j],j-1)+nums[j]
                m[i][j] = max(m1,m2)
            else:
                m[i][j] = m2
            print m
            return m[i][j]
        
    print total - 2*dp(sum,n-1)
    #isum = reduce(lambda x,y:x+y,[1 for i in xrange(sum+1) for j in xrange(n) if m[i][j]==-1])
    #a2 = n*(sum+1)-sum+n
    #print a2, a2-isum
# iterative map dp
def iteMapDP(n,nums):
    total = reduce(lambda x,y:x+y,nums)
    sum = total/2
    m = []
    for i in range(n):
        m.append({})

    def dp(i,j):
        if i in m[j]:
            return m[j][i]
        else:
            if i == 0:
                m[j][i]=0
            elif j == 0:
                if i >= nums[0]:
                    m[j][i]=nums[0]
                else:
                    m[j][i] = 0
            else:
                m2 = dp(i,j-1)
                if i-nums[j]>=0:
                    m1 = dp(i-nums[j],j-1)+nums[j]
                    m[j][i] = max(m1,m2)
                else:
                    m[j][i] = m2
            return m[j][i]
        
    print total - 2*dp(sum,n-1)
# my dp
def myDP(n,nums):
    pass

iteMapDP(n,nums)
