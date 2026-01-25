import math

n = int(input().strip())
counts = list(map(int, input().split())) # keep a count of availablke paper

papers = {i: counts[i - 2] for i in range(2, n + 1)}

def long_side(i: int) -> float: # define a function for long side for reusability
    return 2 ** (-(2 * i - 1) / 4)

need = 1  # need to create 1 sheet of A1

tape = 0.0
for i in range(2, n + 1):
    tape += need * long_side(i) # calculate the length of tape for ith join

    required = 2 * need 
    avail = papers[i]

    if avail >= required:
        print(f"{tape:.12f}")
        raise SystemExit

    need = required - avail

print("impossible")