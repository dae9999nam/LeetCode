class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        n = len(nums)
        nums_sort = sorted(nums)
        res = []
        for i in range(n):
            idx = nums_sort.index(nums[i])
            res.append(idx)
        return res


