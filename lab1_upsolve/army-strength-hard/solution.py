import sys

# read all tokens
data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

idx = 0
t = int(data[idx])
idx += 1

# print("t", t)

results = []

for case_id in range(t):
    if idx >= len(data):
        break
    g_count = int(data[idx])
    m_count = int(data[idx + 1])
    idx += 2

    # print("case", case_id, "g", g_count, "m", m_count)

    max_g = 0
    for _ in range(g_count):
        val = int(data[idx])
        idx += 1
        if val > max_g:
            max_g = val

    # print("max_g", max_g)

    max_m = 0
    for _ in range(m_count):
        val = int(data[idx])
        idx += 1
        if val > max_m:
            max_m = val

    # print("max_m", max_m)

    if max_g >= max_m:
        results.append("Godzilla")
    else:
        results.append("MechaGodzilla")

sys.stdout.write("\n".join(results))
