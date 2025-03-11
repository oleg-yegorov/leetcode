from typing import List

import pytest

# You are given an integer array height of length n. There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1

        max_area = 0
        while left_ptr < right_ptr:
            max_area = max(min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr), max_area)
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area


@pytest.mark.parametrize('height, res', [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
])
def test_max_area(height: List[int], res: int):
    assert Solution().maxArea(height) == res