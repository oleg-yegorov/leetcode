import math

import pytest


class Solution:
    def intToRoman(self, num: int) -> str:
        R = [["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"], ["M"]]

        ans = ""
        for i in range(4):
            d = int(num % (math.pow(10, 1)))
            num -= d
            num /= 10

            if d == 0:
                continue

            s = ""
            if d < 4:
                s = R[i][0] * d
            elif d == 4:
                s = R[i][0] + R[i][1]
            elif d == 5:
                s = R[i][1]
            elif d < 9:
                s = R[i][1] + (R[i][0] * (d-5))
            else:
                s = R[i][0] + R[i][2]

            ans = s + ans

        return ans


@pytest.mark.parametrize('s, res', [
    (3749, "MMMDCCXLIX"),
    (58, "LVIII"),
    (1994, "MCMXCIV")
])
def test_int_to_roman(s: int, res: str):
    assert Solution().intToRoman(s) == res
