

import sys

INF = 10**18

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    p = 0
    out = []

    while True:
        n = int(data[p]); k = int(data[p + 1]); p += 2
        if n == 0 and k == 0:
            break

        L = [0] * n
        R = [0] * n
        total = 0

        for i in range(n):
            L[i] = int(data[p]); R[i] = int(data[p + 1]); p += 2
            total += L[i] + R[i]

        # dp[c][state] = min closed value so far, state: 0=close none, 1=close L, 2=close R
        dp = [[INF, INF, INF] for _ in range(k + 1)]
        dp[0][0] = 0
        if k >= 1:
            dp[1][1] = L[0]
            dp[1][2] = R[0]

        for i in range(1, n):
            ndp = [[INF, INF, INF] for _ in range(k + 1)]

            for c in range(k + 1):
                a0, a1, a2 = dp[c]

                # prev = 0
                if a0 != INF:
                    # cur = 0
                    if a0 < ndp[c][0]:
                        ndp[c][0] = a0
                    # cur = 1
                    if c + 1 <= k:
                        v = a0 + L[i]
                        if v < ndp[c + 1][1]:
                            ndp[c + 1][1] = v
                    # cur = 2
                    if c + 1 <= k:
                        v = a0 + R[i]
                        if v < ndp[c + 1][2]:
                            ndp[c + 1][2] = v

                # prev = 1 (closed L last row, so can't close R this row)
                if a1 != INF:
                    # cur = 0
                    if a1 < ndp[c][0]:
                        ndp[c][0] = a1
                    # cur = 1
                    if c + 1 <= k:
                        v = a1 + L[i]
                        if v < ndp[c + 1][1]:
                            ndp[c + 1][1] = v

                # prev = 2 (closed R last row, so can't close L this row)
                if a2 != INF:
                    # cur = 0
                    if a2 < ndp[c][0]:
                        ndp[c][0] = a2
                    # cur = 2
                    if c + 1 <= k:
                        v = a2 + R[i]
                        if v < ndp[c + 1][2]:
                            ndp[c + 1][2] = v

            dp = ndp

        best_closed = min(dp[k][0], dp[k][1], dp[k][2])
        out.append(str(total - best_closed))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()