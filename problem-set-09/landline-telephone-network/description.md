# Problem D - Landline Telephone Network

The mayor of RMCity wants to create a secure landline telephone network for emergency use in case of serious disasters when the city is cut off from the outside world. Some pairs of buildings in the city can be directly connected with a wire telephone line and the municipality engineers have prepared an estimate of the cost of connecting any such pair.

The mayor needs your help to find the cheapest network that connects all buildings in the city and satisfies a particular security measure. A call from a building `A` to another building `B` may be routed through any simple path in the network, that is, a path that does not have any repeated building. There are also some insecure buildings that one or more persons with serious criminal records live in. The mayor wants only communications intended for these insecure buildings to reach them. In other words, no communication from any building `A` to any building `B` should pass through any insecure building `C` in the network, where `C` is different from `A` and `B`.

## Input

The first line contains three integers `n`, `m`, and `p`, where `1 <= n <= 1000` is the number of buildings, `0 <= m <= 10000` is the number of possible direct connections between a pair of buildings, and `0 <= p < n` is the number of insecure buildings.

The buildings are numbered from `1` to `n`. The second line contains `p` distinct integers between `1` and `n` (inclusive), which are the numbers of insecure buildings.

Each of the next `m` lines contains three integers `x_i`, `y_i`, and `l_i`, describing one potential direct line, where `x_i` and `y_i` are distinct buildings the line connects and `l_i` (`1 <= l_i <= 10000`) is the estimate of the cost of connecting these buildings. There is at most one direct link between any two buildings in these `m` lines.

## Output

Display the cost of the cheapest network satisfying the security measure if it is possible. Otherwise, display `impossible`.

## Sample Input 1

```text
4 6 1
1
1 2 1
1 3 1
1 4 1
2 3 2
2 4 4
3 4 3
```

## Sample Output 1

```text
6
```

## Sample Input 2

```text
4 3 2
1 2
1 2 1
2 3 7
3 4 5
```

## Sample Output 2

```text
impossible
```
