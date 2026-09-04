# [049]. Groups Anagram

**Difficulty:** Medium

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Example 1:

```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

Example 2:

```python
Input: strs = [""]

Output: [[""]]
```

Example 3:

```python
Input: strs = ["a"]

Output: [["a"]]
```

Constraints:

```python
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
```

## Approach

1. Define dictionary and use `sorted str` as key and append each str to the dictionary.

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Anagram`, `Dictionary`
