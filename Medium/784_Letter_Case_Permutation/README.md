# [#784]. Letter Case Permutation

**Difficulty:** Medium

## Problem Description

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

```python
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```

Example 2:

```python
Input: s = "3z4"
Output: ["3z4","3Z4"]
```

Constraints:

```python
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
```

## Approach

1. Define a function that append to result when the length of element is same as `s`

2. For each position(character), letter branches into two recursive call

3. Digits do not branch

## Complexity Analysis

- **Time Complexity:** O(N\*2^N)
- **Space Complexity:** O(N\*2^N)

## Tags

`Backtracking`, `Recursion`
