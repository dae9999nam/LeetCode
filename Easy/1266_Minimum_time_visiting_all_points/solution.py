class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        x, y = points[0][0], points[0][1]
        n = len(points)
        for i in range(1, n):
            dx = abs(points[i][0] - x)    
            dy = abs(points[i][1] - y)

            if dx == dy:
                count += dx
            else:
                if dx > dy:
                    count += dx
                else:
                    count += dy
            x, y = points[i][0], points[i][1]
        return count

