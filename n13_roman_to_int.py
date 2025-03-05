import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'O': 0}

        s += 'O'
        i = 0
        sum = 0
        while i < len(s) - 1:
            if d[s[i]] >= d[s[i + 1]]:
                sum += d[s[i]]
            else:
                sum -= d[s[i]]

            i += 1

        return sum


@pytest.mark.parametrize('s, res', [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
])
def test_roman_to_int(s: str, res: int):
    assert Solution().romanToInt(s) == res
