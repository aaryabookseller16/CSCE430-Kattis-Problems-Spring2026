import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

states = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]

t = data[0]
idx = 1
out = []

for _ in range(t):
    m = data[idx]
    idx += 1

    prefs = []
    for _ in range(m):
        prefs.append(data[idx:idx + 8])
        idx += 8

    dp = [0] * 8
    for s in range(8):
        best_end = -1
        best_rank = 10**9

        for bit in range(3):
            nxt = s ^ (1 << bit)
            rank = prefs[m - 1][nxt]
            if rank < best_rank:
                best_rank = rank
                best_end = nxt

        dp[s] = best_end

    for i in range(m - 2, -1, -1):
        new_dp = [0] * 8

        for s in range(8):
            best_end = -1
            best_rank = 10**9

            for bit in range(3):
                nxt = s ^ (1 << bit)
                end_state = dp[nxt]
                rank = prefs[i][end_state]
                if rank < best_rank:
                    best_rank = rank
                    best_end = end_state

            new_dp[s] = best_end

        dp = new_dp

    out.append(states[dp[0]])  # voting starts from NNN

sys.stdout.write("\n".join(out))
