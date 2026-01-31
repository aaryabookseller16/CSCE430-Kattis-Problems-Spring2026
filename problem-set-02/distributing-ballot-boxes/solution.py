import sys

# flip this to True if you want the debug prints to show
DEBUG = False


def debug(*args):
    if DEBUG:
        print("[debug]", *args, file=sys.stderr)


def boxes_needed(populations, max_per_box):
    """how many boxes do we need if no box can exceed max_per_box"""
    total = 0
    for a in populations:
        # ceil(a / max_per_box)
        need = (a + max_per_box - 1) // max_per_box
        total += need
        debug("city pop", a, "needs", need, "boxes for M=", max_per_box)
    debug("total boxes needed:", total)
    return total


def solve_case(populations, B):
    # simple bounds for binary search
    total_pop = sum(populations)
    max_pop = max(populations)

    # lower bound: at least average, also consider giving all extra boxes to biggest city
    low1 = (total_pop + B - 1) // B
    extra = B - len(populations) + 1  # >= 1 since B >= N
    low2 = (max_pop + extra - 1) // extra
    low = max(1, low1, low2)
    high = max_pop

    debug("initial bounds:", low, high)

    # binary search on the answer M
    while low < high:
        mid = (low + high) // 2
        need = boxes_needed(populations, mid)
        debug("try M=", mid, "need=", need, "B=", B)
        if need <= B:
            high = mid
        else:
            low = mid + 1
        debug("updated bounds:", low, high)

    debug("final M=", low)
    return low


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    results = []

    while idx + 1 < len(data):
        N = int(data[idx]); B = int(data[idx + 1]); idx += 2
        debug("read N,B:", N, B)
        if N == -1 and B == -1:
            break
        pops = []
        for _ in range(N):
            pops.append(int(data[idx])); idx += 1
        debug("populations:", pops)
        ans = solve_case(pops, B)
        results.append(str(ans))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
