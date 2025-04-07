# Dynamic Bounding Boxes 

## Skill Description

S5. Implement an *efficient* solution to a computational problem using advanced data structures and advanced techniques.

## Assignment Instructions

### Background

The bounding box of a set of three-dimensional points is the smallest enclosing axis-aligned rectangular box that contains all the points. Essentially, it is the box formed by the minimum and maximum x-values among all the points, and for the y-values, and for the z-values. For example, in two dimensions, the rectangle shown is the smallest bounding box for the displayed points.

### Problem

Write a program that maintains a set of three-dimensional points with labels and supports the following operations:

1. `INSERT LABEL X Y Z`: Insert the three-dimensional point p with the given label and coordinates x,y,z. If the point with the given `LABEL` already exists, then `UPDATED <LABEL>` should be output and the point should move to the new location. Otherwise, `ADDED <LABEL>` should be output.
2. `DELETE LABEL`: Delete the point with the given `LABEL`. If the point does not exist, the message `POINT DOES NOT EXIST` should be output. Otherwise, `DELETED <LABEL>` should be output (and the point should be removed from the set).
3. BBX: Output the area of the bounding box containing all the points currently in the set.

You can assume the following:

- All input lines will be valid.
- All labels will use the letters A-Z and be no longer than 10 characters.
- All coordinates will be integer values in range -1,000,000 to 1,000,000

**Your code MUST BE EFFICIENT. It should run in O(n log n) time and use O(n) space.**

### Input and Output

The first line of the input is the number N of instructions to support. This is followed by N lines of the above described type of operations.

The output consists of a single line for each operation given depending on the result of the operation (as described above).

### Sample

Here is an example input to illustrate:

```bash
8
INSERT BOB 1 1 1
INSERT ALICE 0 2 4
INSERT CHUCK 4 5 -6
BBX
INSERT ALICE 0 2 14
BBX
DELETE CHUCK
BBX
```

Here is the corresponding output (with some commentary in the <---- part):

```bash
ADDED BOB
ADDED ALICE
ADDED CHUCK
160    <--- (4-0)*(5-1)*(4-(-6))
UPDATED ALICE
320    <--- (4-0)*(5-1)*(14-(-6))
DELETED CHUCK
13     <--- (1-0)*(2-1)*(14-1)
```

### Brainstorming

#### INSERT LABEL X Y Z
- Check that label exists
- If yes update point
- If no add point
- Update bounding box
- `ADDED <LABEL>` if new point
- `UPDATED <LABEL>` if point moved

#### DELETE LABEL
- Check if label exists
- If yes remove point
- If no print `POINT DOES NOT EXIST`
- If deleted update bounding box
    - Might need to recalculate if point at boundary
- `DELETED <LABEL>` if successful
- `POINT DOES NOT EXIST` if not found

#### BBX
- Calculate box volume
  - $(x_1 - x_2) * (y_1 - y_2) * (z_1 - z_2)$
- Output volume

#### Implementation
- Can use a dictionary for the points
    - `Key: label (string), Value: (x, y, z) coordinates`
- Need to store min and max of x, y, z coordinates
    - `min_x, max_x, min_y, max_y, min_z, max_z`