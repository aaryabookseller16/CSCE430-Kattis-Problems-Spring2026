# Problem C: Bridge Automation

A bridge can be raised to let boats pass. The bridge is unavailable to road
traffic while it is being raised, while it is raised, and while it is being
lowered.

Rules:

- raising the bridge takes 60 seconds
- lowering the bridge takes 60 seconds
- once the bridge is fully raised, each boat takes 20 seconds to pass
- boats arrive at known times
- no boat may wait more than 30 minutes, which is 1800 seconds
- the bridge may stay raised while waiting for the next boat if that helps

Find the minimum total number of seconds during which the bridge is unavailable
to road traffic.

## Input

The first line contains an integer `N`, the number of boats.

```text
1 <= N <= 4000
```

The next `N` lines each contain one integer `Ti`, the arrival time of boat `i`,
in seconds.

The arrival times are sorted increasingly, and no two boats arrive within 20
seconds of each other.

## Output

Print one integer: the minimum total unavailable time for road traffic.

## Sample Input 1

```text
2
100
200
```

## Sample Output 1

```text
160
```

## Sample Input 2

```text
3
100
200
2010
```

## Sample Output 2

```text
250
```

## Sample Input 3

```text
3
100
200
2100
```

## Sample Output 3

```text
300
```

## Idea

Split the boats into groups. Each group is handled during one bridge opening.

For a group from boat `i` to boat `j`, open the bridge as late as possible for
boat `i`, so boat `i` waits exactly 1800 seconds unless that is unnecessary.
Then the cost is:

```text
120 + max(20 * number_of_boats, last_arrival - first_arrival - 1780)
```

Use dynamic programming to decide where the groups should start and end.
