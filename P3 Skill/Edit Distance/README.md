# Edit Distance

## Skill Description

P3. Implement an efficient solution to a problem that uses dynamic programming

## Assignment Instructions

Let us modify the edit distance with the following requirements:

- Substitute: Change one character for another - cost is 5
- Insert: Insert one character into S - cost is 3
- Delete: Delete one character from S - cost is 3
- Swap: Swap two neighboring characters - cost is 2 (e.g. `cat` can swap `ca` to become `act`. Once swapped those two characters can't be changed again. So you can't swap `ct` to get `atc`)

Write a program that takes two strings as input and outputs the edit distance as defined above along with the specific changes neded (the strings along the way).
