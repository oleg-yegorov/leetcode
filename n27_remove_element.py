from typing import List

import pytest


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


@pytest.mark.parametrize('nums, val, expected_nums',[
    ([3, 2, 2, 3], 3, [2, 2]),
    ([0,1,2,2,3,0,4,2], 2, [0,1,4,0,3])
])
def test_remove_element(nums: List[int], val: int, expected_nums: List[int]):
    k = Solution().removeElement(nums, val)

    assert k == len(expected_nums)
    nums = nums[:k]
    nums.sort()
    assert nums == expected_nums
