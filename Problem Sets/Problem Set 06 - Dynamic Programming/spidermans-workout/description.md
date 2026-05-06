# Problem D - Spiderman's Workout

Staying fit is important for every superhero, and Spiderman is no exception. Every day he undertakes a climbing exercise in which he climbs a certain distance, rests for a minute, then climbs again, rests again, and so on. The exercise is described by a sequence of distances `d1, d2, ... , dM` telling how many meters he is to climb before the first rest break, before the second break, and so on.

From an exercise perspective it does not really matter if he climbs up or down at the `i`-th climbing stage, but it is practical to sometimes climb up and sometimes climb down so that he both starts and finishes at street level. Obviously, he can never be below street level. Also, he would like to use as low a building as possible, since he does not like to admit that he is actually afraid of heights. The building must be at least `2` meters higher than the highest point his feet reach during the workout.

He wants your help in determining the sequence of up and down movements for the distances. The answer must be legal: it must start and end at street level (`0` meters above ground) and may never go below street level. Among all legal solutions, choose one that minimizes the required building height. When looking for a solution, you may not reorder the distances.

To illustrate, assume there are `20 20 20 20` meters to cover. He can then either climb up, up, down, down or up, down, up, down. Both are legal, but the second one is better, since the height reaches only `20` instead of `40`. If the distances are `3 2 5 3 1 2`, an optimal legal solution is to go up, up, down, up, down, down. Note that for some distance sequences there is no legal solution at all, for example `3 4 2 1 6 4 5`.

## Input

The first line of the input contains an integer `N` giving the number of test scenarios, `1 <= N <= 10`. The following `2N` lines specify the test scenarios, two lines per scenario:

- The first line gives a positive integer `M <= 40`, the number of distances.
- The second line contains `M` positive integers, the distances.

For every scenario, the total distance climbed, that is, the sum of the distances in that scenario, is at most `1000`.

## Output

For each input scenario a single line should be output. This line should either be the string `IMPOSSIBLE` if no legal solution exists, or it should be a string of length `M` containing only the characters `U` and `D`, where the `i`-th character indicates if Spiderman should climb up or down at stage `i`.

If there are several different legal and optimal solutions, output any one of them.

## Sample Input 1

```text
3
4
20 20 20 20
6
3 2 5 3 1 2
7
3 4 2 1 6 4 5
```

## Sample Output 1

```text
UDUD
UUDUDD
IMPOSSIBLE
```
