
import sys
import math

D = sys.stdin.read().strip().split()
if D:
    target_distance = int(D[0])

    # once b is so large that (b^2 - (b-1)^2) = 2b-1 exceeds the target, larger b cannot help
    largest_no = (target_distance + 1) // 2 + 2

    for later_frame in range(largest_no + 1):
        later_sq = later_frame * later_frame
        earlier_sq = later_sq - target_distance
        if earlier_sq < 0:
            continue
        earlier_frame = int(math.isqrt(earlier_sq))
        if earlier_frame * earlier_frame == earlier_sq:
            print(earlier_frame, later_frame)
            break
    else:
        print("impossible")