from typing import List


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals:
            if res[-1][1] < interval[0]:
                res.append(interval)
            elif interval[0] <= res[-1][1] <= interval[1]:
                res[-1][1] = interval[1]

        return res


def test_merge_intervals():
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge([[1,4],[4,5]]) == [[1,5]]
