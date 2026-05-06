# Problem B - Going to Seed

The Great Seedling is a mythical spirit that supposedly rewards whoever catches it with farm crops that remain in bloom forever. Rumor has it that before dawn tonight, it will come to Sweet Apple Acres, the Apple family's farm.

Applejack and Apple Bloom want to catch the Great Seedling to help with their massive orchard this season. They have decided to watch the farm closely enough to track it. Catching the Seedling is not easy, though, and they only get one shot. If the Great Seedling becomes aware that it is being hunted, it will flee and never be found again.

There are `N` trees in Sweet Apple Acres, labeled `1` through `N` from left to right. The Great Seedling is hidden behind exactly one of these trees.

In one half-hour, Applejack and Apple Bloom may each choose one consecutive range of trees to observe. During that half-hour, the Great Seedling will jump from its current tree to an adjacent tree. It does this very quietly, but when it lands, exactly that tree rustles.

At the end of the half-hour, Applejack and Apple Bloom each report whether they noticed a rustle somewhere in the range they were watching. They cannot tell exactly which tree rustled, only whether some tree in their watched range did. Their reports are always correct.

Once they are certain where the Great Seedling is, they can rush to that tree and catch it, but they only get one immediate attempt. If they guess wrong, the Seedling will notice and escape for good.

There are only `16` half-hours before sunrise, when the Great Seedling leaves forever. Help them catch it.

## Interaction

First, your program should read a single integer `N` (`2 <= N <= 10^9`) from standard input, the number of trees.

Then you may repeat the following process at most `16` times:

- Print a line of the form `Q l1 r1 l2 r2`, where `1 <= l1 <= r1 <= N` and `1 <= l2 <= r2 <= N`. This means that for the next half-hour, Applejack watches the trees `l1` through `r1`, and Apple Bloom watches the trees `l2` through `r2`. The two ranges may overlap, and they may even be identical.
- After printing such a query, read two integers `u1` and `u2` from standard input, each either `0` or `1`.
  - `u1 = 1` means Applejack observed a rustle in her watched range, and `u1 = 0` means she did not.
  - `u2 = 1` means Apple Bloom observed a rustle in her watched range, and `u2 = 0` means she did not.

When you know the exact tree, print a line of the form `A t`, where `1 <= t <= N`, meaning that the Great Seedling is behind tree `t` and should be captured immediately. Your program should terminate right after printing this.

After every query, flush standard output.

## Sample Interaction

One possible interaction for `N = 6` is shown below:

```text
judge: 6
you:   Q 1 3 5 5
judge: 1 0
you:   Q 2 2 4 4
judge: 0 0
you:   Q 1 4 4 6
judge: 1 1
you:   A 4
```

In that example, the answers are enough to conclude that the Great Seedling must be behind tree `4`.
