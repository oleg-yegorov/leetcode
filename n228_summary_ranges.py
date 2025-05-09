from typing import List


# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        i = 0
        while i < len(nums):
            j = i
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if i == j:
                result.append(f"{nums[j]}")
            else:
                result.append(f"{nums[j]}->{nums[i]}")
            i += 1

        return result


def test_summary_ranges():
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
