import sys

INF = 10**18


def solve_case(k: int, symbols_line: str, table_lines: list[str], queries: list[str]) -> list[str]:
    symbols = symbols_line.split()
    sym_to_idx = {s: i for i, s in enumerate(symbols)}
    idx_to_sym = symbols  # preserve given order for tie-breaks

    # cost[a][b] = time to combine type a then type b
    # res[a][b]  = resulting type after combining a then b
    cost = [[0] * k for _ in range(k)]
    res = [[0] * k for _ in range(k)]

    for r in range(k):
        entries = table_lines[r].split()
        for c in range(k):
            t_str, out_sym = entries[c].split("-")
            cost[r][c] = int(t_str)
            res[r][c] = sym_to_idx[out_sym]

    costM = cost
    resM = res

    answers = []

    for s in queries:
        s = s.strip()
        m = len(s)
        arr = [sym_to_idx[ch] for ch in s]

        # dp[l][r][t] = min time to make substring l..r into type t
        dp = [[[INF] * k for _ in range(m)] for __ in range(m)]

        # reachable[l][r] = list of types t where dp[l][r][t] is not INF
        # we only loop over these to avoid useless work
        reachable = [[[] for _ in range(m)] for __ in range(m)]

        # base: one char is already its own type, cost 0
        for pos in range(m):
            t0 = arr[pos]
            dp[pos][pos][t0] = 0
            reachable[pos][pos].append(t0)

        # build up by increasing substring length
        for length in range(2, m + 1):
            for l in range(0, m - length + 1):
                r = l + length - 1

                dp_lr = dp[l][r]          # local ref (faster)
                reach_lr = reachable[l][r]

                # try every split point
                for mid in range(l, r):
                    left_types = reachable[l][mid]
                    if not left_types:
                        continue
                    right_types = reachable[mid + 1][r]
                    if not right_types:
                        continue

                    left_dp = dp[l][mid]
                    right_dp = dp[mid + 1][r]

                    # loop over reachable types only
                    for a in left_types:
                        ta = left_dp[a]
                        # local row refs for a (big speedup)
                        cost_a = costM[a]
                        res_a = resM[a]

                        for b in right_types:
                            tb = right_dp[b]
                            new_time = ta + tb + cost_a[b]
                            out_t = res_a[b]

                            old = dp_lr[out_t]
                            if new_time < old:
                                if old == INF:
                                    # first time we discovered this resulting type for [l..r]
                                    reach_lr.append(out_t)
                                dp_lr[out_t] = new_time

        # choose best final type for full string [0..m-1]
        best_time = INF
        best_type = 0
        final_row = dp[0][m - 1]
        for t in range(k):
            val = final_row[t]
            if val < best_time:
                best_time = val
                best_type = t
            elif val == best_time and t < best_type:
                best_type = t

        answers.append(f"{best_time}-{idx_to_sym[best_type]}")

    return answers


def main() -> None:
    data = sys.stdin.buffer.read().splitlines()
    if not data:
        return

    # decode lazily line-by-line (keeps things fast enough and simple)
    lines = [line.decode().strip() for line in data]
    p = 0
    out = []

    while p < len(lines):
        if lines[p] == "":
            p += 1
            continue

        k = int(lines[p])
        p += 1
        if k == 0:
            break

        symbols_line = lines[p]
        p += 1

        table_lines = lines[p:p + k]
        p += k

        n = int(lines[p])
        p += 1

        queries = lines[p:p + n]
        p += n

        out.extend(solve_case(k, symbols_line, table_lines, queries))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()