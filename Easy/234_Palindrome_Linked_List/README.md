# [#234]. Palindrome Linked List

**Difficulty:** Easy

## Problem Description

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

## Approach

1. Measure length of linked list
2. Set middle point and append first half of linked list in stack
3. Compare elements in stack to the remaining linked list

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Tags

`Linked List`
