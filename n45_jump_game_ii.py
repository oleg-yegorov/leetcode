from typing import List

import pytest


# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
# if you are at nums[i], you can jump to any nums[i + j] where: 0 <= j <= nums[i] and i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can
# reach nums[n - 1].
class Solution:
    # На каждом следующем шаге мы имеем интервал с самыми дальними достижимыми элементами.
    def canJump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        ach_start = 0
        ach_end = 0
        step_count = 0

        while True:
            new_ach_end = max([(i + nums[i]) for i in range(ach_start, ach_end + 1)])
            step_count += 1

            if new_ach_end >= n - 1:
                return step_count

            ach_start = ach_end + 1
            ach_end = new_ach_end


@pytest.mark.parametrize('nums, res', [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
])
def test_can_jump_ii(nums: List[int], res: int):
    assert Solution().canJump(nums) == res
