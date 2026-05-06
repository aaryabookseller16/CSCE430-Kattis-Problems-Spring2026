# Problem A - Breaking Bad

Walter was once a promising chemist. Now he teaches high school students chemistry, and has recently been diagnosed with lung cancer. In both desperation and excitement he decides to use his chemistry skills to produce illegal drugs and make quick money for his family. He forms a partnership with one of his old students, Jesse, who has some experience with the drug scene.

Now Walter and Jesse are preparing for their first "cook". They have a list of items they need to buy, but they have realized it may be suspicious to buy certain pairs of items during the same shopping trip. They decide to divide the items between themselves so that each of them can make one trip to the store without buying any suspicious pair together.

Your task is to find such a division, or determine that it is impossible.

## Input

The first line contains an integer `N` (`1 <= N < 100000`), the number of items they want to buy.

The next `N` lines contain the names of the items. All item names are distinct. A name consists of at most 20 lowercase English letters or underscores, and is non-empty.

The next line contains an integer `M` (`0 <= M < 100000`), the number of suspicious pairs.

The next `M` lines each contain the names of two different items that form a suspicious pair. Each suspicious pair appears exactly once.

## Output

If it is possible to divide the items between Walter and Jesse, output two lines:

- the first line should contain the names of the items Walter should buy
- the second line should contain the names of the items Jesse should buy

If there are multiple valid solutions, output any of them. If it is impossible, output `impossible`.

## Sample Input 1

```text
5
battery_acid
drain_cleaner
antifreeze
cold_medicine
lantern_fuel
2
cold_medicine battery_acid
antifreeze lantern_fuel
```

## Sample Output 1

```text
lantern_fuel drain_cleaner battery_acid
antifreeze cold_medicine
```

## Sample Input 2

```text
3
fuel
lighter
knife
3
fuel lighter
lighter knife
knife fuel
```

## Sample Output 2

```text
impossible
```
