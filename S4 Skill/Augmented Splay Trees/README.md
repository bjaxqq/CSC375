# S4 Skill

## Skill Description

S4. Develop a correct implementation of a given advanced data structure.

## Assignment Instructions

We discussed in class the Splay Tree. For this assignment, you are tasked with implementing a version of the splay tree that supports a range count operation. That is, it should be able to efficiently report how many elements fall within a given range.

The data structure should support the following operations:
- `insert(e)`: Insert an element e into the structure. We will assume the tree stores integer values.
- `delete(e)`: Delete element e from the structure.
- `range(a, b)`: Report how many elements in the structure fall between a (inclusive) and b (inclusive).

For example, if we performed the following sequence of operations:

```java
SplayTree<Integer> tree = new SplayTree<>();
tree.insert(1);
tree.insert(10);
tree.insert(3);
tree.insert(5);
tree.insert(8);
tree.insert(12);
tree.delete(5);
tree.delete(3);
tree.insert(4);
int res = tree.rangeCount(2,10); // Should return 3 (4, 8, and 10 are between 2 and 10)
```

The approach works by maintaining an additional field called size with every node that represents the size of the subtree rooted at that node. Whenever an element is inserted into or deleted from a subtree, the corresponding size of that subtree should increase or decrease by one. In addition, when a splay rotation is performed, the sizes of the affected nodes should be updated.