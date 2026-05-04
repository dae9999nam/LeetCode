class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        min_diff = float("inf")
        for i in range(1, len(arr)):
            temp = abs(arr[i] - arr[i-1])
            if min_diff >= temp and arr[i] > arr[i-1]:
                if min_diff > temp:
                    ans = []
                min_diff = temp
                ans.append([arr[i-1], arr[i]])
        return ans