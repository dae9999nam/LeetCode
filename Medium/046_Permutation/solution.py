class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                res.append(current_path[:])
                return
            for n in nums:
                if n not in current_path:
                    current_path.append(n)
                    backtrack(current_path)
                    current_path.pop()
        backtrack([])
        return res
