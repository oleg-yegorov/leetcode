from typing import List

import pytest

import utility


# You are given an integer array nums. You are initially positioned at the array's first index, and each element
# in the array represents your maximum jump length at that position. Return true if you can reach the last index,
# or false otherwise.
class SolutionInPlace:
    # Здесь я на месте делаю отрицательными те значения, до которых я могу дотянуться. Если дотягиваюсь до
    # последнего - тогда True
    def canJump(self, nums: List[int]) -> bool:
        nums[0] = -nums[0]
        n = len(nums)

        if n == 1:
            return True

        for i in range(n):
            for j in range(i + 1, i + 1 - nums[i]):
                if j == n - 1:
                    return True
                nums[j] = min(nums[j], -nums[j])

        return False


class SolutionFaster:
    # Здесь я вычисляю максимальный индекс, до которого я могу дотянуться от текущей точки. Если он больше
    # предыдущего максимального индекса, то тогда я его обновляю
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        max_ach = 0
        for i in (range(n)):
            if i > max_ach:
                return False

            max_ach = max(i + nums[i], max_ach)
            if max_ach >= n - 1:
                return True

        return False


@pytest.mark.parametrize('nums, res', [
    ([0], True),
    ([1], True),
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__))
def test_can_jump(solution_class, nums: List[int], res: bool):
    assert solution_class().canJump(nums) == res
