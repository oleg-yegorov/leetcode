from typing import List


# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented
# as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
# between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number
# of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # after Youtube
        res = len(points)
        points.sort(key=lambda x: x[0])

        prev = points[0]
        for i in range(1, res):
            if prev[1] >= points[i][0]:
                prev[0] = max(prev[0], points[i][0])
                prev[1] = min(prev[1], points[i][1])
                res -= 1
            else:
                prev = points[i]

        return res

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        i = 0
        arrow_count = 0
        int = points[0]
        while i < len(points):
            int[0] = max(points[i][0], int[0])
            int[1] = min(points[i][1], int[1])
            if int[1] - int[0] < 0:
                arrow_count += 1
                int = points[i]
            i += 1

        return arrow_count + 1


def test_find_minimum_arrow_shots():
    assert Solution().findMinArrowShots([[13,16],[2,8],[1,6],[7,12]]) == 3
    assert Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
