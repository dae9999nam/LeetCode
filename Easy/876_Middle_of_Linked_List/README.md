# [876]. Middle of the Linked List

**Difficulty:** Easy

## Problem Description

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

## Approach

1. Set two pointers with one takes one step each while the other takes two steps

2. When the two step pointer gets to the end, one step pointer will arrive at the half.

3. Return the one step pointer

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Linked List`, `Two Pointers`
