class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        if n < 3:
            return 0

        best = 0
        i = 0

        while i < n - 1:
            # 1) find uphill start
            while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1

            start = i

            # 2) climb up
            while i < n - 1 and arr[i] < arr[i + 1]:
                i += 1
            peak = i

            # 3) climb down
            while i < n - 1 and arr[i] > arr[i + 1]:
                i += 1
            end = i

            # valid mountain must have both an up and a down
            if start < peak < end:
                best = max(best, end - start + 1)

            # if no downhill happened, we need to move forward at least 1
            if i == peak:
                i += 1

        return best