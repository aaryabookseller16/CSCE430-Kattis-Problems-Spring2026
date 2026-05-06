n, t = map(int,input().split())
a,b, c,cur = map(int, input().split())
MOD = 1000000007
seen  = [-1] * (c + 1)
made=[]
# print("start", cur)

while len(made) < n and seen[cur] == -1:
    seen[cur]  = len(made)
    made.append(cur)
    cur = ((a * cur+b) % c) + 1
    # if len(made) % 100000 == 0:
    #     print("generated", len(made))
cnt = [0]*(c + 1)

if len(made) == n:
    for x in made:
        cnt[x]=cnt[x] + 1
else:
    first_cycle_spot = seen[cur]
    cycle_size  = len(made)-first_cycle_spot
    j = 0
    while j < first_cycle_spot:
        cnt[made[j]] = cnt[made[j]] + 1
        j=j + 1
    left  = n - first_cycle_spot
    repeat = left//cycle_size
    extra  = left % cycle_size
    j = first_cycle_spot
    while j < len(made):
        cnt[made[j]]  = cnt[made[j]] + repeat
        j = j + 1
    j = 0
    while j < extra:
        cnt[made[first_cycle_spot + j]] = cnt[made[first_cycle_spot+j]] + 1
        j = j + 1
# print("cycle done")
used=0
solved = 0
pen  = 0
minute = 1
while minute <= c:
    have=cnt[minute]
    if have > 0:
        can = (t - used)//minute
        if can > have:
            can = have

        if can > 0:
            solved=solved + can
            pen = pen + can * (used % MOD)
            pen = pen + minute*can * (can + 1)//2
            pen=pen % MOD
            used = used + minute * can
            # print("taking", can, "of", minute)
        if can < have:
            break
    minute=minute + 1

print(solved, pen)
