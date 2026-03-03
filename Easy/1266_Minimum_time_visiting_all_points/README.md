# [1266]. Minimum Time Visiting All Points

**Difficulty:** Easy

## Problem Description

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

## Approach

1. Set the first element of array as starting point

2. calculate `dx`, `dy` for each element and add to count

3. return count

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Array`
