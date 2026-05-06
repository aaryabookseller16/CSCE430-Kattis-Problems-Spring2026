import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

idx = 0
a = data[idx]
d = data[idx + 1]
idx += 2

up_h = []
up_t = []
for _ in range(a):
    up_h.append(data[idx])
    up_t.append(data[idx + 1])
    idx += 2

down_h = []
down_t = []
for _ in range(d):
    down_h.append(data[idx])
    down_t.append(data[idx + 1])
    idx += 2

up_time = [0]
up_height = [0]
for i in range(a):
    up_time.append(up_time[-1] + up_t[i])
    up_height.append(up_height[-1] + up_h[i])

down_time = [0]
down_drop = [0]
for i in range(d):
    down_time.append(down_time[-1] + down_t[i])
    down_drop.append(down_drop[-1] + down_h[i])

total_height = up_height[-1]
up_total_time = up_time[-1]
down_total_time = down_time[-1]

left = 0.0
right = float(max(up_total_time, down_total_time))

up_ptr = 0
down_ptr = 0

for _ in range(100):
    mid = (left + right) / 2.0

    if mid >= up_total_time:
        up_pos = float(total_height)  # he already reached the top
    else:
        while up_ptr > 0 and up_time[up_ptr] > mid:
            up_ptr -= 1
        while up_ptr + 1 < len(up_time) and up_time[up_ptr + 1] < mid:
            up_ptr += 1

        up_pos = float(up_height[up_ptr])
        if up_ptr < a:
            span_t = up_t[up_ptr]
            span_h = up_h[up_ptr]
            up_pos += span_h * (mid - up_time[up_ptr]) / span_t

    if mid >= down_total_time:
        down_pos = 0.0  # he already got back to the bottom
    else:
        while down_ptr > 0 and down_time[down_ptr] > mid:
            down_ptr -= 1
        while down_ptr + 1 < len(down_time) and down_time[down_ptr + 1] < mid:
            down_ptr += 1

        down_pos = float(total_height - down_drop[down_ptr])
        if down_ptr < d:
            span_t = down_t[down_ptr]
            span_h = down_h[down_ptr]
            down_pos -= span_h * (mid - down_time[down_ptr]) / span_t

    if up_pos >= down_pos:
        right = mid  # they already met by now
    else:
        left = mid  # still below the descending monk

ans = (left + right) / 2.0
sys.stdout.write(f"{ans:.6f}\n")
