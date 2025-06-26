from typing import List
from collections import defaultdict

import pytest

import utility


class SolutionCount:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount = 0
        res = 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if maxCount < count[n]:
                maxCount = count[n]
                res = n

        return res


class SolutionCountBoyerMoore:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)

        return res


class Solution:
    # my first attempt: remove not equal elements.
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                if i + 1 != j:
                    t = nums[j]
                    nums[j] = nums[i + 1]
                    nums[i + 1] = t

                i += 2
                j = j + 1

        return nums[j] if j < len(nums) else nums[i]


@pytest.mark.parametrize('nums, major', [
    ([6, 5, 5], 5),
    ([3, 3, 4], 3),
    ([3, 3, 3, 2], 3),
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2)
])
@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[defaultdict]))
def test_majority_element(solution_class, nums: List[int], major: int):
    r = solution_class().majorityElement(nums)
    assert r == major
