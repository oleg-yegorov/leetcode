from typing import List

import pytest


# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0


@pytest.mark.parametrize('target, nums, res', [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
])
def test_min_subarray_len(target: int, nums: List[int], res: int):
    assert Solution().minSubArrayLen(target, nums) == res
