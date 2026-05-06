import sys

INF = 10**18
lines = sys.stdin.read().strip().split("\n")
# split input into lines so we can process step by step
i = 0

out_lines = []

while i < len(lines):
    # number of different component types
    k = int(lines[i].strip())
    i += 1
    if k == 0:
        break

    # read the list of symbols (types)
    symbols = lines[i].split()
    i += 1

    # map each symbol to an integer index for matrix access
    symbols_to_index = {sym: idx for idx, sym in enumerate(symbols)}
    index_to_symbol = symbols[:]  # index -> symbol

    # cost[a][b] = time needed to combine type a followed by type b
    cost = [[0] * k for _ in range(k)]
    # result[a][b] = resulting type index after combining a and b
    result = [[0] * k for _ in range(k)]

    for row in range(k):
        entries = lines[i].split()
        i += 1
        for col in range(k):
            time_str, res_sym = entries[col].split('-')
            cost[row][col] = int(time_str)
            result[row][col] = symbols_to_index[res_sym]

    # print("Constructed cost matrix:", cost)
    # print("Constructed result matrix:", result)
    n = int(lines[i].strip())
    i += 1

    queries = []
    for _ in range(n):
        queries.append(lines[i].strip())
        i += 1

    # solve each query string independently using interval DP
    for s in queries:
        m = len(s)
        # convert characters of the string into their index form
        arr = [symbols_to_index[ch] for ch in s]

        # dp[l][r][t] = min time to make substring l..r into type t
        dp = [[[INF] * k for _ in range(m)] for __ in range(m)]
        #print(f"Initialized DP table for string '{s}' of length {m}")

        # base case: single character costs 0 to become itself
        for pos in range(m):
            dp[pos][pos][arr[pos]] = 0

        # build answers for increasing substring lengths
        for length in range(2, m + 1):
            for l in range(0, m - length + 1):
                r = l + length - 1

                # try every possible split point of the interval
                for mid in range(l, r):
                    left = dp[l][mid]
                    right = dp[mid + 1][r]

                    # try all possible resulting types from left side
                    for a in range(k):
                        ta = left[a]
                        if ta == INF:
                            continue
                        # try all possible resulting types from right side
                        for b in range(k):
                            tb = right[b]
                            if tb == INF:
                                continue

                            c = result[a][b]
                            new_time = ta + tb + cost[a][b]
                            if new_time < dp[l][r][c]:
                                dp[l][r][c] = new_time

        # after filling dp, choose the best final type for the whole string
        best_time = INF
        best_type = 0
        for t in range(k):
            if dp[0][m - 1][t] < best_time:
                best_time = dp[0][m - 1][t]
                best_type = t
            elif dp[0][m - 1][t] == best_time and t < best_type:
                best_type = t

        out_lines.append(f"{best_time}-{index_to_symbol[best_type]}")

# print all answers at the very end
print("\n".join(out_lines))