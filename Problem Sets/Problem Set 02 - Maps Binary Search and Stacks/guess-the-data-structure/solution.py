
import sys
import heapq
from collections import deque

# read input
data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

idx = 0
out = []

while idx < len(data):
    n = int(data[idx])
    idx += 1

    # flags for which structures are still possible
    is_stack = True
    is_queue = True
    is_pq = True

    stack = []
    queue = deque()
    pq = []  # max-heap using negatives

   #print(" new case n=", n, file=sys.stderr)

    for _ in range(n):
        if idx + 1 >= len(data):
            break  # just in case, input should be valid though
        op = int(data[idx]); x = int(data[idx + 1]); idx += 2

        #print(" op", op, x, file=sys.stderr)

        if op == 1:
            # push into all still-possible structures
            if is_stack:
                stack.append(x)
            if is_queue:
                queue.append(x)
            if is_pq:
                heapq.heappush(pq, -x)
        else:
            #try poppig
            if is_stack:
                if not stack or stack[-1] != x:
                    is_stack = False
                else:
                    stack.pop()

            if is_queue:
                if not queue or queue[0] != x:
                    is_queue = False
                else:
                    queue.popleft()

            if is_pq:
                if not pq or -pq[0] != x:
                    is_pq = False
                else:
                    heapq.heappop(pq)

        #print(" flags", is_stack, is_queue, is_pq, file=sys.stderr)

    cnt = (1 if is_stack else 0) + (1 if is_queue else 0) + (1 if is_pq else 0)
    if cnt == 0:
        out.append("impossible")
    elif cnt > 1:
        out.append("not sure")
    else:
        if is_stack:
            out.append("stack")
        elif is_queue:
            out.append("queue")
        else:
            out.append("priority queue")

print("\n".join(out))
