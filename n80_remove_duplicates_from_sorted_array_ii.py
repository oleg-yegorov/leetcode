from typing import List

import pytest


# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
# unique element appears at most twice. The relative order of the elements should be kept the same.
class Solution:
    # Два указателя. Но сохраняем статус того, что только что был уже дубль.
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        eq = False
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                eq = False
            else:
                if not eq:
                    j += 1
                    nums[j] = nums[i]
                eq = True

        return j + 1


@pytest.mark.parametrize('nums, val, expected_nums', [
    ([1, 1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ([1, 1, 2], 3, [1, 1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 9, [0, 0, 1, 1, 2, 2, 3, 3, 4])
])
def test_remove_element(nums: List[int], val: int, expected_nums: List[int]):
    k = Solution().removeDuplicates(nums)

    assert k == len(expected_nums)
    assert nums[:k] == expected_nums
