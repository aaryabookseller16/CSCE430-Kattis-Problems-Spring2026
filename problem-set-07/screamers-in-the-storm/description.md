# Problem D - Screamers in the Storm

On Mars, even though its atmosphere is very thin, winds can blow with unexpected force. The effect can grow even stronger in narrow and deep canyons close to the equator. The floor of one of these canyons is extremely flat and is used for transport because its steep walls provide partial shielding from cosmic radiation. Over time, sand has accumulated in the canyon. It is blown by the wind into sizeable sand dunes which obstruct the transport. The dunes form one long string of dunes stretched along the canyon floor.

The arrangement of the dunes is not stable. Raging sand storms often remodel the dunes into a different string. Violent movement of sand masses in the storm produces an eerie sound for which the dunes are known as "Screamers in the storm".

Detailed measurements of the dunes revealed that the height of adjacent dunes, expressed in Martian meters, is always a small positive integer. Moreover, probably due to wind interference effects in the canyon, the heights of two adjacent dunes are different, unless they are both `1`.

In fact, the heights of two adjacent dunes are always relatively prime, that is, they share no common factor bigger than `1`.

To model the dune behavior, the number of all possible configurations of the dunes in the string has to be established.

## Input

The input contains one line with two integers `K`, `N` (`1 <= K <= 66`, `1 <= N <= 10^18`), the maximum possible height of a dune and the number of dunes in the string of dunes.

## Output

Print the number of different strings of dunes. Output the result modulo `10^9 + 7`.

## Sample Input 1

```text
3 4
```

## Sample Output 1

```text
41
```

## Sample Input 2

```text
2 4
```

## Sample Output 2

```text
8
```

## Sample Input 3

```text
42 75097099101114
```

## Sample Output 3

```text
673977658
```
