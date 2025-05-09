from typing import List


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
class Solution:
    def merge_intervals(self, inc: dict[int], dec: dict[int], n: int, m: int) -> None:
        inc[dec[n]] = inc[m]
        dec[inc[m]] = dec[n]

        del inc[m]
        del dec[n]

    def longestConsecutive2(self, nums: List[int]) -> int:
        inc = {}
        dec = {}
        for n in nums:
            if n in inc or n in dec:
                continue

            inc[n] = n
            dec[n] = n

            if n + 1 in inc:
                self.merge_intervals(inc, dec, n, n + 1)
            if n - 1 in dec:
                self.merge_intervals(inc, dec, n - 1, n)

        return max(value - key + 1 for key, value in inc.items()) if inc else 0

    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0
        for el in s:
            if el - 1 in s:
                continue

            size = 1
            while el + 1 in s:
                size += 1
                el = el + 1

            longest = max(size, longest)
        return longest


def test_longest_cons():
    assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
    assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert Solution().longestConsecutive([1,0,1,2]) == 3
    assert Solution().longestConsecutive([]) == 0
