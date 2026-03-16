# [#020]. Valid Parentheses

**Difficulty:** Easy

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

Constraints:

`1 <= s.length <= 104`
`s consists of parentheses only '()[]{}'.`

## Approach

1. Create a stack and for each open parentheses, append close parentheses to the stack

2. If `s` is not open parenthese, `stack.pop()` and compare them

3. If they are not equal, or stack is empty, or after checking all `s` but stack is not empty, return `False`. Otherwise return `True`

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Tags

`Stack`, `Simulation`
