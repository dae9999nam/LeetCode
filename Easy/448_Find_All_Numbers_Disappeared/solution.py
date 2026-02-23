class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        s = set(nums)
        missing = []
        for i in range(1, (l+1)):
            if i not in s:
                missing.append(i)
        return missing
