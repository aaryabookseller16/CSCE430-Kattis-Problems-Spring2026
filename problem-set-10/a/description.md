# Cantina of Babel

Characters in Star Wars each speak one language, but they often understand other languages too. Two characters can converse if they can exchange messages in both directions, possibly through a chain of translators.

You are given the characters currently in the cantina. Some of them may not be able to communicate with others. Find the size of the smallest set of characters that must leave so that all remaining characters can converse.

## Input

The first line contains an integer `N` (`1 <= N <= 100`), the number of characters in the cantina.

The next `N` lines each describe one character:

- the character's name, which is distinct
- the language the character speaks
- zero to twenty additional languages the character understands

Every character also understands the language they speak.

All names and languages are strings of length `1` to `15` using lowercase letters, uppercase letters, digits, and hyphens. Items on a line are separated by single spaces.

## Output

Print a single integer: the size of the smallest set of characters that must leave so that all remaining pairs of characters can converse.

## Sample Input 1

```text
7
Jabba-the-Hutt Huttese
Bib-Fortuna Huttese Basic
Boba-Fett Basic Huttese
Chewbacca Shyriiwook Basic
Luke Basic Jawaese Binary
Grakchawwaa Shyriiwook Basic Jawaese
R2D2 Binary Basic
```

## Sample Output 1

```text
2
```

## Sample Input 2

```text
6
Fran French Italian
Enid English German
George German Italian
Ian Italian French Spanish
Spencer Spanish Portuguese
Polly Portuguese Spanish
```

## Sample Output 2

```text
4
```
