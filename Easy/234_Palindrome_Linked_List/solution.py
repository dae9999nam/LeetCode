# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        cur = head
        step = 0
        while cur:
            step += 1
            cur = cur.next
        stack = []
        cur = head
        for _ in range(step // 2):
            stack.append(cur.val)
            cur = cur.next
        if step % 2 == 1:
            cur = cur.next

        while cur:
            top = stack.pop()
            if cur.val != top:
                return False
            cur = cur.next
        
        return True
    
    """
    Better solution with O(N) and O(1)
    if not head or not head.next:
            return True

        # 1) find middle (second middle for even)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) reverse second half starting at slow
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # now prev is head of reversed second half

        # 3) compare first half and reversed second half
        p1, p2 = head, prev
        while p2:  # second half is shorter or equal
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
    """