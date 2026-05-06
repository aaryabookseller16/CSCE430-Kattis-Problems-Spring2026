# Secret Message

Jack and Jill developed a special encryption method so they can enjoy conversations without worrying about eavesdroppers. Here is how it works:

Let L be the length of the original message, and let M be the smallest square number greater than or equal to L. Add (M - L) asterisks to the message, giving a padded message with length M. Use the padded message to fill a table of size K x K, where K^2 = M. Fill the table in row-major order (top to bottom rows, left to right within a row). Rotate the table 90 degrees clockwise. The encrypted message is read in row-major order from the rotated table, omitting any asterisks.

For example, if the original message is `iloveyouJack`, then L = 12 and M = 16, so we pad to `iloveyouJack****`. Fill a 4 x 4 table row-wise, rotate it clockwise, and then read row-wise while skipping `*` to get the secret message.

---

## Input

- The first line contains an integer N (1 <= N <= 100), the number of original messages.
- The following N lines each contain a message to encrypt.
- Each message contains only letters a-z or A-Z and has length 1 <= L <= 10000.

---

## Output

For each original message, output the secret message.

---

## Example

### Input
```
2
iloveyoutooJill
TheContestisOver
```

### Output
```
iteiloylloooJuv
OsoTvtnheiterseC
```
