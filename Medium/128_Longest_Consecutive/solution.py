class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        count = 1
        max_count = 0
        if n < 1:
            return 0

        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                count += 1
                if count > max_count:
                    max_count = count
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                count = 1
        return max(max_count, count)

        
