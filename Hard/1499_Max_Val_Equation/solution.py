from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        dq = deque()   # stores pairs (x, y-x), decreasing by (y-x)
        ans = float('-inf')

        for x, y in points:
            # remove points too far away
            while dq and x - dq[0][0] > k:
                dq.popleft()

            # if we have a valid previous point, compute candidate
            if dq:
                ans = max(ans, x + y + dq[0][1])

            # current value to add for future points
            cur = y - x

            # maintain decreasing order of (y-x)
            while dq and dq[-1][1] <= cur:
                dq.pop()

            dq.append((x, cur))

        return ans