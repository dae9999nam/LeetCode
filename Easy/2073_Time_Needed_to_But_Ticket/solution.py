class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        if not tickets:
            return 0
        queue = tickets
        count = 0
        is_k = False
        while queue:
            cur = queue.pop(0)
            if k >= 0:
                k -= 1
            else:
                break
            cur -= 1
            count += 1
            if cur > 0 and k == -1:
                k = len(queue)
                queue.append(cur)
            elif cur > 0:
                queue.append(cur)
        return count




        
                
