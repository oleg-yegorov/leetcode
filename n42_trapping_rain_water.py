from typing import List

import pytest


# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
class Solution:
    def trap_peaks(self, height: List[int]) -> int:
        height.insert(0, 0)
        height.append(0)

        # find peaks
        peaks = []
        i = 0
        ascend = True
        while i < len(height) - 1:
            if ascend:
                ascend = True if height[i] <= height[i+1] else False
                if not ascend:
                    peaks.append(i)
            else:
                ascend = True if height[i] < height[i+1] else False
            i += 1

        # remove bad peaks (that are located between higher peaks)
        has_bad_peak = True
        while has_bad_peak:
            for i in range(1, len(peaks) - 1):
                if height[peaks[i]] <= height[peaks[i-1]] and height[peaks[i]] <= height[peaks[i+1]]:
                    del peaks[i]
                    break
            else:
                has_bad_peak = False

        # fill water between good peaks
        rain_water = 0
        for i in range(len(peaks) - 1):
            local_water_level = min(height[peaks[i]], height[peaks[i+1]])
            for j in range(peaks[i] + 1, peaks[i+1]):
                diff = local_water_level - height[j]
                if diff > 0:
                    rain_water += diff

        return rain_water

    # two pointers
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans


@pytest.mark.parametrize('height, res', [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([0], 0),
    ([1, 1, 1], 0),
])
def test_trapping_rain_water(height: List[int], res: int):
    assert res == Solution().trap(height)
