# Problem B - Building Dependencies

A Makefile is a file that specifies dependencies between different source code files. When one source code file changes, that file needs to be recompiled, and whenever one of its dependencies is recompiled, that file also needs to be recompiled.

Given the set of Makefile rules and a changed file, output the set of files that must be recompiled, in an order that satisfies the dependencies. In other words, if a file `X` and one of its dependencies `Y` both need to be recompiled, then `Y` must appear before `X` in the output.

## Input

The input consists of:

- one line with one integer `n` (`1 <= n <= 100000`), the number of Makefile rules
- `n` lines, each containing one Makefile rule; a rule starts with `f:` where `f` is a filename, followed by the filenames of the dependencies of `f`
- one line with one string `c`, the filename of the changed file

Filenames are strings of between 1 and 10 lowercase letters. Exactly `n` different filenames appear in the input, and each appears exactly once as the `f` in a Makefile rule. Each file has at most 5 dependencies.

The rules are such that no two files depend on each other, directly or indirectly.

## Output

Output all files that need to be recompiled, in any order such that all dependencies are satisfied. If there are multiple valid answers, you may output any of them.

## Sample Input 1

```text
6
gmp:
solution: set map queue
base:
set: base gmp
map: base gmp
queue: base
gmp
```

## Sample Output 1

```text
gmp
map
set
solution
```
