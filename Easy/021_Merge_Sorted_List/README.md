# [#021]. Merge Two Sorted List

**Difficulty:** Easy

## Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

## Approach

1. Create one dummy node and set tow pointers that point to each list
2. compare each nodes and set the samller valued node to `tail.next`
3. Connect leftover nodes and return the dummy list

## Complexity Analysis

- **Time Complexity:** O(N+M)
- **Space Complexity:** O(1)

## Tags

`Linked List`, `Tow Pointer`
