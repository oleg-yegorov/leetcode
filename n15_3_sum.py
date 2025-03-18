from typing import List

import pytest


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    # Hash-table approach
    def twoSum2(self, nums: List[int], i: int) -> List[List[int]]:
        seen = set()
        r = []
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                r.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
        return r

    # Two pointer approach
    def twoSum(self, nums: List[int], i: int) -> List[List[int]]:
        lo, hi = i + 1, len(nums) - 1
        r: List[List[int]] = []
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum == 0:
                r.append([nums[i], nums[lo], nums[hi]])
                hi -= 1
                lo += 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
            elif sum > 0:
                hi -= 1
            else:
                lo += 1

        return r

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        r = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            r.extend(self.twoSum2(nums, i))

        return r


@pytest.mark.parametrize('nums, res', [
    ([0,0,0,0], [[0,0,0]]),
    # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1, 0, 1, 2, -1, -4], [[-1, 1, 0], [-1, 2, -1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
])
def test_3sum(nums: List[int], res: List[int]):
    assert Solution().threeSum(nums) == res
