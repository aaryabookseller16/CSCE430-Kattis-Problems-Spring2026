# Problem F: Character Development

A writer has `N` characters. Any group of at least two characters can have a
relationship that may need to be explored.

If there are no characters or only one character, there are no relationships.
If there are three characters, the possible relationships are:

- each pair
- the group of all three

So for `N = 3`, the answer is `4`.

Given `N`, count how many relationships need to be explored.

## Input

The input contains a single integer `N`, where:

```text
0 <= N <= 500
```

## Output

Print one integer: the number of relationships among the characters.

## Sample Input 1

```text
1
```

## Sample Output 1

```text
0
```

## Sample Input 2

```text
3
```

## Sample Output 2

```text
4
```

## Idea

Every subset of characters is either:

- empty
- one character
- at least two characters

There are `2^N` total subsets. Remove the empty subset and the `N` single-person
subsets.

The answer is:

```text
2^N - N - 1
```
