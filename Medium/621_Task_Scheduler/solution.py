class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        max_freq = 0
        
        for val in freq.values():
            if val > max_freq:
                max_freq = val
        max_count = 0
        for val in freq.values():
            if val == max_freq:
                max_count += 1
        
        return max(len(tasks), (max_freq-1) * (n+1) + max_count)


