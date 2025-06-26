from typing import List

import pytest


# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
class Solution:
    # Метод деления отрезка пополам
    def findMin(self, nums: List[int]) -> int:
        start_index = 0
        end_index = len(nums) - 1

        if nums[start_index] <= nums[end_index]:
            return nums[start_index]

        while end_index - start_index > 1:
            mid_index = (end_index - start_index) // 2 + start_index

            if nums[start_index] > nums[mid_index]:
                end_index = mid_index
            else:
                start_index = mid_index

        return nums[end_index]


@pytest.mark.parametrize('nums, ret', [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11)
])
def test_find_minimum_in_rotated_sorted_array(nums, ret):
    assert(Solution().findMin(nums) == ret)
