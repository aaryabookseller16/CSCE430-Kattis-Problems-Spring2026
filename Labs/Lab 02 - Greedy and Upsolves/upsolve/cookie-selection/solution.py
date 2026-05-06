# --- old code commented out (TLE) ---
# import sys
#
# # flip this to True if you wanna see a ton of debug prints
# DEBUG = False
#
#
# def debug(*args):
#     if DEBUG:
#         print("[debug]", *args, file=sys.stderr)
#
#
# def main():
#     lines = sys.stdin.read().splitlines()
#     cookies = []  # just a plain list, we will sort it when we need
#     out = []
#
#     debug("total lines:", len(lines))
#
#     for raw in lines:
#         s = raw.strip()
#         if s == "":
#             # ignore blank lines, just in case
#             continue
#
#         if s == "#":
#             # need to send one cookie (upper median)
#             if not cookies:
#                 # problem says this won't happen, but just in case
#                 debug("got # but cookies empty???")
#                 continue
#
#             debug("before sort:", cookies)
#             cookies.sort()  # super lazy way
#             debug("after sort:", cookies)
#
#             idx = len(cookies) // 2  # upper median position (0-based)
#             chosen = cookies[idx]
#             out.append(str(chosen))
#             debug("picked", chosen, "at idx", idx, "len", len(cookies))
#
#             cookies.pop(idx)
#             debug("after pop:", cookies)
#         else:
#             # should be a number
#             try:
#                 d = int(s)
#             except ValueError:
#                 debug("weird line??", s)
#                 continue
#
#             cookies.append(d)
#             debug("added", d, "cookies now", len(cookies))
#
#     sys.stdout.write("\n".join(out))
#
#
# if __name__ == "__main__":
#     main()


import sys
import heapq

DEBUG = False


def debug(*args):
    if DEBUG:
        print("[debug]", *args, file=sys.stderr)


def rebalance(low, high):
    if len(high) < len(low):
        move = -heapq.heappop(low)
        heapq.heappush(high, move)
        debug("rebalance low->high", move)
    elif len(high) > len(low) + 1:
        move = heapq.heappop(high)
        heapq.heappush(low, -move)
        debug("rebalance high->low", move)


def add_cookie(x, low, high):
    if not high or x >= high[0]:
        heapq.heappush(high, x)
        debug("push to high", x)
    else:
        heapq.heappush(low, -x)  # max-heap via negatives
        debug("push to low", x)
    rebalance(low, high)


def pop_upper_median(low, high):

    # high should never be empty here if input is valid
    med = heapq.heappop(high)
    debug("pop median", med)
    # after removing, fix sizes
    if len(high) < len(low):
        move = -heapq.heappop(low)
        heapq.heappush(high, move)
        debug("fix sizes after pop", move)
    return med


def main():
    data = sys.stdin.buffer.read().split()
    low = []   # max-heap (store negatives)
    high = []  # min-heap (store normal values)
    out = []

    debug("tokens:", len(data))

    for tok in data:
        if tok == b"#":
            # send a cookie (upper median)
            if not high and not low:
                debug("got # but empty??")
                continue
            out.append(str(pop_upper_median(low, high)))
        else:
            # number line
            x = int(tok)
            add_cookie(x, low, high)
            debug("sizes", len(low), len(high))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()