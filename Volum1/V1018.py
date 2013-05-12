import sys

ll = sys.stdin.readline().split()

n = int(ll[0])
q = int(ll[1])

tree = {}
m = [{} for x in xrange(n+1)]

for line in sys.stdin:
    ll = line.split()
    start = int(ll[0])
    end = int(ll[1])
    apples = int(ll[2])
    if not start in tree:
        tree[start] = []
    tree[start].append((end,apples))
    if not end in tree:
        tree[end] = []
    tree[end].append((start,apples))

def buildTree(tree,node,root):
    children = tree[node]
    temp_children = []
    for c in children:
        if c[0] != root:
            temp_children.append(c)
    tree[node] = temp_children
    for c in temp_children:
        buildTree(tree,c[0],node)
    
    
def f(i,rest):
    if rest<=0:
        return 0
    if rest in m[i]:
        return m[i][rest]

    max_apple = 0
    children = tree[i]
    if len(children) == 0:
        return 0
    elif len(children) == 1:
        max_apple = children[0][1] + f(children[0][0],rest-1)
        m[i][rest]=max_apple
        return max_apple
    else:
        ma1 = children[0][1] + f(children[0][0],rest-1)
        ma2 = children[1][1] + f(children[1][0],rest-1)
        max_apple = max([ma1,ma2])
        for k in xrange(0,rest-2+1):
            ma = children[0][1]+children[1][1]+f(children[0][0],rest-2-k)+f(children[1][0],k)
            if max_apple<ma:
                max_apple = ma
        m[i][rest]=max_apple
        return max_apple

buildTree(tree,1,0)
print f(1,q)

