class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if target - numbers[left] == numbers[right]:
                break
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]