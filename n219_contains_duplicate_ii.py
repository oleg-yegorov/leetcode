from typing import List


# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that
# nums[i] == nums[j] and
# abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s_ind = 0
        e_ind = k
        s = set(nums[s_ind:e_ind + 1])

        if min(len(nums), k + 1) > len(s):
            return True

        while e_ind + 1 < len(nums):
            s.remove(nums[s_ind])
            s_ind += 1
            e_ind += 1
            s.add(nums[e_ind])

            if len(s) < k + 1:
                return True

        return False


def test_contains_nearby_duplicate():
    # assert not Solution().containsNearbyDuplicate([1], 0)
    # assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 10)
    # assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
