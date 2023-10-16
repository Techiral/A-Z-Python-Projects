# Dice Puzzle

A six-sided dice is a small cube with a different number of pips on each face(side), 
ranging from 1 to 6. On any two opposite sides of the cube, the number of pips adds up to 7;
that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, 3 and 4.

There are N dice lying on a table, each showing the pips on its top face. In one move, 
you can take one dice and rotate it to an adjacent face. For example, you can rotate a dice that 
show 1 so that it shows 2, 3, 4 or 5. however, it can't show 6 in single move, because 
the face with one pip and six pips visible are on opposite side rather than adjacent.

You want to show the same number of pips on the top faces of all N dice. Given that each of 
the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Input Specification:
The array A with consisting of N integers describing the number of pips (from 1 to 6)

Example:

`A: [1, 1, 6]`

Output: `2`

Explanation:
The only optimal answer is to rotate the last dice so that it shows one pip. It is necessary to use two rotations to achive this.

`A: [1, 6, 2, 3]`

Output: `3`

Explanation:
For instance, you can make all dice show 2: just rotate each diece which is not showing 2 (and notice that for each dice you can do this in one move).

**How to run?**

```
 python dice.py
```