class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n):
            temp = target - nums[i]
            if temp in nums:
                idx = nums.index(temp)
                if idx not in ans and idx!=i:
                    ans.append(i)
                    ans.append(idx)

        ans.sort()
        return ans