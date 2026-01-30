import sys

# just grab all nums
nums = sys.stdin.buffer.read().split()
if not nums:
    sys.exit(0)

i = 0
s = int(nums[i]); i += 1
t = int(nums[i]); i += 1
n = int(nums[i]); i += 1

walk = list(map(int, nums[i:i + n + 1])); i += n + 1
ride = list(map(int, nums[i:i + n])); i += n
gap = list(map(int, nums[i:i + n])); i += n

# print("s", s, "t", t, "n", n)
# print("walk", walk)
# print("ride", ride)
# print("gap", gap)

time = s

for k in range(n):
    # walk part
    add1 = walk[k]
    time = time + add1

    # wait part
    g = gap[k]
    mod = time % g
    need = g - mod
    if mod == 0:
        need = 0
    time = time + need

    # ride part
    add2 = ride[k]
    time = time + add2

    # print("after", k, time)

# last walk
last_walk = walk[n]
time = time + last_walk

# print("final", time)
ok = False
if time <= t:
    ok = True

if ok:
    print("yes")
else:
    print("no")