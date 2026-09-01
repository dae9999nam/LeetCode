# [#003]. Longest Substring without Repeat

**Difficulty:** Medium

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

Example 1:

```python
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```

Example 2:

```python
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```python
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

```python
0 <= s.length <= 10^5
s consists of English letters, digits, symbols and spaces.
```

## Approach

1. Define a `set` to store a seen character

2. For every character, if `current character` is not in the `set`, add the character in the set and move right.

3. Else (i.e. `current character` in the `set`), measure the length of current characters and empty the `set`

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(max(N,M))

## Tags

`Sliding Window`, `Hash Table`
