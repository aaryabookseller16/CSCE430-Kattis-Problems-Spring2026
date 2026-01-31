# Cookie Selection

## Problem
A cookie production line sends freshly baked cookies to a holding area. Each cookie has a diameter in nanometers. From time to time, the packaging unit requests a cookie to be sent for packaging.

Your strategy is always to send the **median** cookie (using the *upper median* when the count is even):
- If there are `c` cookies in the holding area and they were sorted by diameter,
  - if `c` is odd, send the cookie at position `(c + 1) / 2`,
  - if `c` is even, send the cookie at position `(c / 2) + 1`.

Process the input stream and output the diameter of each cookie sent for packaging.

## Input
Each line is either:
- a positive integer `d` (a new cookie with diameter `d` nm arrives), or
- the symbol `#` (send one cookie for packaging using the rule above).

Constraints:
- At most 600000 lines of input.
- The holding area is empty before the first cookie arrives.
- No request `#` will occur when the holding area is empty.
- `d <= 300000000` (30 cm).

## Output
For each `#`, output one line with the diameter (in nm) of the cookie sent, in the order they are sent.

## Sample Input 1
```text
1
2
3
4
#
#
#
#
```

## Sample Output 1
```text
3
2
4
1
```

## Sample Input 2
```text
1
#
2
#
3
#
4
#
```

## Sample Output 2
```text
1
2
3
4
```
