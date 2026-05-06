# Juggler

Check a juggling siteswap pattern. A pattern is a string of digits where digit `d` means the throw lands `d` beats later. Balls landing on the same beat collide and make the pattern invalid. The number of balls in a valid pattern equals the average of its digits.

## Input
One pattern per line (unknown count, end of file). Each line is a string of digits.

## Output
For each pattern, print `VALID <balls>` if no collisions occur, otherwise `INVALID`.
