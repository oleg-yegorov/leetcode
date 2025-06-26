from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        pr = 1
        for i in range(n - 1):
            pr *= nums[i]
            answer[i + 1] = pr

        pr = 1
        for i in range(n - 1, 0, -1):
            pr *= nums[i]
            answer[i - 1] *= pr

        return answer
