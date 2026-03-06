class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, n-1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    left_val = nums[l]
                    right_val = nums[r]
                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1
        return res