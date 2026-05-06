# Table Solution: Cat Coat Colors

## What this version changes
This markdown explains `solution_table.py`. The approach is hardcoded genotype probability table plus enumeration. This version lists complete genotype triples for each visible parent color directly, then enumerates gametes and kitten outcomes.

## Step-by-step algorithm
1. Read the female and male visible colors.
2. Look up all possible hidden genotype triples for each parent color with their probabilities.
3. For each parent genotype pair, list possible gametes for black, dilution, and red genes.
4. Enumerate each combination of mother and father gametes and kitten sex.
5. Convert the kitten genotype/sex into a visible color.
6. Accumulate probabilities by color and print them sorted.

## Example walkthrough
A Blue parent maps to black choices BB or Bb with dilution dd, so every kitten receives a dilute allele from that parent.

## Complexity
Constant time for the fixed gene model; memory O(number of colors).

## Important details
The main solution builds the same options with more branching; this version stores more of the biology as explicit tables.
