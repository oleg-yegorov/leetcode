from typing import List

import pytest


# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        for g in range(Solution().gcd(len(nums), k)):
            t = nums[g]
            i = g
            j = (len(nums) - k + i) % len(nums)

            while j != g:
                nums[i] = nums[j]
                i = j
                j = (len(nums) - k + i) % len(nums)

            nums[i] = t


class SolutionRotateByOne:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range((len(nums)- k) % len(nums)):
            nums.append(nums[0])
            del nums[0]


class SolutionRotateSlicing:
    def rotate(self, nums: List[int], k: int) -> None:
        k = (len(nums) - k) % len(nums)
        res = (list(nums[0:k]))
        del nums[0:k]
        nums.extend(res)


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


@pytest.mark.parametrize('nums, k, to_be_nums', [
    ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
    ([1, 2], 3, [2, 1]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100])
])
@pytest.mark.parametrize('solution_class', [Solution, Solution2, SolutionRotateSlicing, SolutionRotateByOne])
def test_rotate_array(solution_class, nums: List[int], k: int, to_be_nums: List[int]):
    nums_copy = nums.copy()
    solution_class().rotate(nums_copy, k)
    assert nums_copy == to_be_nums
