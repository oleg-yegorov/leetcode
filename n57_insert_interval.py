from typing import List


# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
# the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low = []
        high = []

        start = newInterval[0]
        end = newInterval[1]
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                low.append(interval)
                continue

            if interval[0] <= newInterval[0] <= interval[1]:
                start = interval[0]
            if interval[0] <= newInterval[1] <= interval[1]:
                end = interval[1]

            if interval[0] > newInterval[1]:
                high = intervals[i:]

        return [*low, [start, end], *high]


def test_insert_interval():
    assert Solution().insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
