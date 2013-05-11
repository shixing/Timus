import sys

# DFS

sys.setrecursionlimit(10005)
n = int(sys.stdin.readline().strip())
if n>10000:
    print 0
    sys.exit()
ns = []
satis = []
for line in sys.stdin:
    nn = int(line.strip())
    ns.append(nn)
    satis.append({})

stack = []
state_stack = []
return_slot = None

stack.append((n-1,0,1))
state_stack.append('CALL')

while len(stack)>0:
    (i,sum,least) = stack[-1]
    state = state_stack[-1]

    if state == 'CALL': # call the function
        if sum == 0 and least <= 0:
            return_slot = (True,0)
            state_stack[-1]='RETURN'
            continue
        if i<0:
            if least> 0:
                return_slot = (False,2)
                state_stack[-1]='RETURN'
                continue
            else:
                if sum == 0:
                    return_slot = (True, 0)
                    state_stack[-1]='RETURN'
                    continue
                else:
                    return_slot = (False,2)
                    state_stack[-1]='RETURN'
                    continue
        if sum in satis[i]:
            return_slot = satis[i][sum]
            state_stack[-1]='RETURN'
            continue

        state_stack[-1] = 'WAIT1'        
        stack.append( (i-1,sum,least) )

        state_stack.append('CALL')
    
    elif state == 'RETURN':
        del stack[-1]
        del state_stack[-1]
        continue

    elif state == 'WAIT1':
        (s,sum1) = return_slot
        if s==True:
            satis[i][sum] = (True,0)
            return_slot = (True,0)
            state_stack[-1] = 'RETURN'
            continue
        
        state_stack[-1] = 'WAIT2'
        stack.append((i-1,(sum-ns[i])%n, least-1))        
        state_stack.append('CALL')
        continue
    
    elif state == "WAIT2":
        (s,sum2) = return_slot
        if s == True:
            satis[i][sum] = (True,1)
            return_slot = (True,1)
            state_stack[-1]='RETURN'
            continue
        
        satis[i][sum] = (False,2)
        return_slot = (False,2)
        state_stack[-1] = 'RETURN'


def f(i, sum, least):
    if sum == 0 and least <= 0:
        return (True,0)
    if i<0:
        if least > 0:
            return (False,2)
        else:
            if sum == 0:
                return (True,0)
            else:
                return (False,2)
    if sum in satis[i]:
        return satis[i][sum]

    (s,sum2) = f(i-1, (sum - ns[i])%n,least-1)
    if s == True:
        satis[i][sum] = (True,1)
        return (True,1)
    
    (s,sum1) = f(i-1,sum,least)    
    if s==True:
        satis[i][sum] = (True,0)
        return (True,0)
    
    satis[i][sum] = (False,2)
    return (False,2)

#f(n-1,0,1)

if satis[n-1][0][0] == False:
    print 0
else:
    results = []
    idx = n-1
    mod = 0
    while idx>=0:
        pair = satis[idx][mod]
        if pair[1] == 0:
            idx-=1
        elif pair[1] == 1:
            results.append( ns[idx] )
            mod = (mod - ns[idx]) % n
            idx -= 1
        if len(results)>0 and mod == 0:
            break

    print len(results)
    for r in results:
        print r



