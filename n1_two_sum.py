from typing import List

import pytest


class Solution:
    # Создается дополнительная структура - хэш-таблица (словарь).
    # Эта структура хранит структуру массима (значение и индекс), чтобы не можно было решить задачу за один проход.
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[nums[i]] = i

    # Перебор всех возможных пар и сравнение с суммой.
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

    # Метод двух указателей. Которые сходятся к середине. Если один из указателей указывает на нужное значение
    # (левый - на меньший индекс или правый на больший), то второй указатель просто дойдет до своего нужного
    # положение. А так как указатели сходятся на каждом шаге, один из них рано или поздно дойдет. Ну а к этому
    # времени второй не сможет пройти своего положение, потому что тогда уже он будет "притягивать" второй указатель.
    def twoSumTwoPointers(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = nums.copy()
        nums_sorted.sort()

        low_it = 0
        high_it = len(nums) - 1

        while True:
            cur_sum = nums_sorted[low_it] + nums_sorted[high_it]
            if cur_sum > target:
                high_it -= 1
            elif cur_sum < target:
                low_it += 1
            else:
                return [nums.index(nums_sorted[low_it]), len(nums) - 1 - nums[::-1].index(nums_sorted[high_it])]


@pytest.mark.parametrize('nums, target, ret', [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
])
def test_two_sum(nums, target, ret):
    assert(Solution().twoSumTwoPointers(nums, target) in [ret, list(reversed(ret))])
