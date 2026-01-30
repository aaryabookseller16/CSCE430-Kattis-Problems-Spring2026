
# Transit Woes

Everyday Yraglac relies on his city's local transit system to get to class. He leaves his house at time s and needs to arrive by time t. He takes n bus routes in order. Between walking segments and riding buses, you must decide if he arrives on time.

He walks for d0 time to the first bus stop, then after riding bus i he walks for di+1 time to the next stop (or to class after the last bus). Each bus i takes bi time to ride. Each bus i arrives every ci minutes, with the first bus leaving at time 0.

Given the new schedules, determine whether Yraglac can make it to class on time.

---

## Input

- The first line contains three integers s, t, n where 0 <= s <= t <= 1000 and 1 <= n <= 20.
- The second line contains n + 1 integers di (0 <= di <= 1000). d0 is the walk from the house to the first stop, and dn is the walk from the last drop-off to class.
- The third line contains n integers bi (1 <= bi <= 1000), the ride times for each bus.
- The fourth line contains n integers ci (1 <= ci <= 1000), the interval between arrivals for each bus (first bus at time 0).

---

## Output

Output `yes` if Yraglac will be able to get to class in time, otherwise output `no`.

---

## Example 1

### Input
```
0 20 2
2 2 2
5 5
3 5
```

### Output
```
yes
```

## Example 2

### Input
```
0 10 1
3 3
1
8
```

### Output
```
no
```
