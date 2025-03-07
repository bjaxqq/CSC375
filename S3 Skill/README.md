# S3 Skill

## Skill Description

S3. Use advanced data structures, algorithms, and mathematical techniques to solve a computational
problem *efficiently and* analyze its performance.

## Instructions

(From the weekly assessment)

Suppose you are given an array $A$ of $n$ real numbers, another real number $x$, and an integer $k$, with $0<k≤n$. Create an efficient *linear time* $\Theta(n)$ algorithm that can output the $k$ numbers closest to $x$ in $A$. The output does not have to be in sorted order. Note that the array contains *real* numbers so you can't use radix sort for this one! For simplicity, you can assume that there are no duplicates in the array.

For example, if $A=[3.6,9.1,-8.8,1.7,4.1,6.2,-2.3,5.5,1.6,5.3]$, $x=3.1416$ and $k=3$, then the result would be $[3.6,1.7,4.1]$.

***Be sure to also analyze your algorithm's efficiency.***
***Note: I will give credit for an*** $O(n + k \ log \ n)$ ***solution that is described well.***