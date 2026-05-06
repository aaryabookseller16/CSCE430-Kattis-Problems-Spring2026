# Problem B: Brexit

A trading union has `C` countries and `P` trade partnerships. One country leaves
first. After that, other countries may leave too.

If at least half of a country's original trading partners have already left, that
country will also leave.

You are citizen of country `X`. Determine whether your country eventually leaves
the union.

## Input

The first line contains four integers:

```text
C P X L
```

where:

- `C` is the number of countries
- `P` is the number of trade partnerships
- `X` is your home country
- `L` is the first country to leave

Constraints:

- `2 <= C <= 200000`
- `1 <= P <= 300000`
- `1 <= X <= C`
- `1 <= L <= C`

The next `P` lines each contain two integers `A` and `B`, meaning countries `A`
and `B` are trading partners.

No pair of countries is listed more than once. Initially, every country has at
least one trading partner.

## Output

Print:

- `leave` if country `X` eventually leaves
- `stay` otherwise

## Sample Input 1

```text
4 3 4 1
2 3
2 4
1 2
```

## Sample Output 1

```text
stay
```

## Sample Input 2

```text
5 5 1 1
3 4
1 2
2 3
1 3
2 5
```

## Sample Output 2

```text
leave
```

## Idea

Use a queue of countries that have left. For every country that leaves, increase
the "lost partners" count for its neighbors. If a neighbor has now lost at least
half of its original partners, it leaves too.
