# Problem E: Cat Coat Colors

Cat coat color is controlled by three genes in this simplified model:

- black gene: `B` or `b`
- dilution gene: `D` or `d`
- red gene: `O` or `o`

Black and dilution are normal two-copy genes. Red is sex-linked, so males have
only one red gene while females have two.

The possible non-tortie colors are:

```text
Black
Blue
Chocolate
Lilac
Red
Cream
```

The possible tortie colors, which only happen for female cats with one `O` and
one `o`, are:

```text
Black-Red Tortie
Blue-Cream Tortie
Chocolate-Red Tortie
Lilac-Cream Tortie
```

For cats where a gene does not affect the visible coat color, assume the hidden
gene possibilities are equally likely according to the statement.

## Input

The input contains two lines.

The first line is the female cat's color.

The second line is the male cat's color.

Each color is written exactly as listed above. The male cat will not be a tortie.

## Output

Print every possible offspring color with positive probability.

Each line should contain:

```text
color probability
```

Sort the output first by decreasing probability, then alphabetically by color
name.

The absolute error of each probability must be less than `10^-9`.

## Sample Input 1

```text
Red
Red
```

## Sample Output 1

```text
Red 0.937500000
Cream 0.062500000
```

## Sample Input 2

```text
Lilac-Cream Tortie
Blue
```

## Sample Output 2

```text
Blue 0.375000000
Cream 0.250000000
Blue-Cream Tortie 0.187500000
Lilac 0.125000000
Lilac-Cream Tortie 0.062500000
```

## Sample Input 3

```text
Blue
Red
```

## Sample Output 3

```text
Black 0.328125000
Black-Red Tortie 0.328125000
Blue 0.109375000
Blue-Cream Tortie 0.109375000
Chocolate 0.046875000
Chocolate-Red Tortie 0.046875000
Lilac 0.015625000
Lilac-Cream Tortie 0.015625000
```

## Idea

List all parent genotypes that could create each visible color. Then try every
possible gamete from both parents and both kitten sexes. Add the probability for
the resulting kitten color.
