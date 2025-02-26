from typing import List

import pytest


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
# unique element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


@pytest.mark.parametrize('nums, val, expected_nums', [
    ([], 0, []),
    ([1, 2, 2], 2, [1, 2]),
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
])
def test_remove_element(nums: List[int], val: int, expected_nums: List[int]):
    k = Solution().removeDuplicates(nums)

    assert k == len(expected_nums)
    assert nums[:k] == expected_nums
