# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        res = []
        while cur:
            if cur in res:
                return True
            else:
                res.append(cur)
            cur = cur.next
        return False
