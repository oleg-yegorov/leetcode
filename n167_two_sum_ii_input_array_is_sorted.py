from typing import List

import pytest


# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
# of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1

        while True:
            sum = numbers[left_ptr] + numbers[right_ptr]
            if sum < target:
                left_ptr += 1
            elif sum > target:
                right_ptr -= 1
            else:
                return [left_ptr + 1, right_ptr + 1]


@pytest.mark.parametrize('nums, target, ret', [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2])
])
def test_two_sum_ii(nums, target, ret):
    assert(Solution().twoSum(nums, target) in [ret, list(reversed(ret))])