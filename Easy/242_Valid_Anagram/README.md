# [242]. Valid Anagram

**Difficulty:** Easy

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

Example 1:

```python
Input: s = "anagram", t = "nagaram"

Output: true
```

Example 2:

```python
Input: s = "rat", t = "car"

Output: false
```

Constraints:

```python
1 <= s.length, t.length <= 5 \* 10^4
s and t consist of lowercase English letters.
```

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Approach

1. The `Anagram` means (i) same characters (ii) same frequency of each characters (iii) order can differ.

2. Compare the length of each `s` and `t`.

3. Check the frequency of each characters in `s` and `t`.

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(k)

## Tags

`dictionary`, `Anagram`
