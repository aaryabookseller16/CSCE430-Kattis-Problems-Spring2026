import math

n,e, p=map(int,input().split())

xs=[]
ys = []

for i in range(n):
    x, y=map(float,input().split())
    xs.append(x)
    ys . append(y)
    # if i % 200 == 0:
    #     print("read point", i)
free=[]
for i in range(n):
    free.append(set())
# the first e houses are already connected through the ground
i=0
while i + 1 < e:
    free[i].add(i + 1)
    free[i+1].add(i)
    i=i+1
for i in range(p):
    a,b=map(int,input().split())
    a=a-1
    b = b -1
    free[a] . add(b)
    free[b].add( a )
    # print("old cable", a, b)
used=[False]*n
best = [10**30]  * n
best[0]=0.0
answer = 00
got=0
while got < n:
    where=-1
    val=10**31
    j=0
    while j < n:
        if not used[j] and best[j] < val:
            val=best[j]
            where =j
        j=j+1
    used[where]=True
    answer=answer + val
    got = got+1
    # if got % 100 == 0:
    #     print("treehouses connected", got)
    j=0
    while j < n:
        if not used[j]:
            if j in free[where]:
                possible=0.0
            else:
                dx=xs[where]-xs[j]
                dy = ys[where] - ys[j]
                possible=math.sqrt(dx * dx+dy*dy)

            if possible < best[j]:
                best[j]=possible
        j =j+1

print("{:.6f}".format(answer))
