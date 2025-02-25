from typing import List

import pytest


# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
class Solution:
    # идем с конца и добавляем старшие элементы.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1

        write_index = m + n + 1
        while n > -1 and m > -1:
            if nums1[m] > nums2[n]:
                nums1[write_index] = nums1[m]
                m -= 1
            else:
                nums1[write_index] = nums2[n]
                n -= 1
            write_index -= 1

        while n > -1:
            nums1[write_index] = nums2[n]
            n -= 1
            write_index -= 1


@pytest.mark.parametrize('nums1, m, nums2, n, res', [
    ([2,0], 1, [1], 1, [1, 2]),
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int, res: List[int]):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res
