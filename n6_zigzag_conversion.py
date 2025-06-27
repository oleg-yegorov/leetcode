import pytest


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strRows = [''] * numRows

        if numRows == 1:
            return s

        j = 1
        strRows[0] += s[0]
        while True:
            for i in range(1, numRows):
                if j < len(s):
                    strRows[i] += s[j]
                    j += 1
                else:
                    return ''.join(strRows)

            for i in range(numRows - 2, -1, -1):
                if j < len(s):
                    strRows[i] += s[j]
                    j += 1
                else:
                    return ''.join(strRows)


@pytest.mark.parametrize('s, numRows, res', [
    ('PAYPALISHIRING', 1, 'PAYPALISHIRING'),
    ('PAYPALISHIRING', 2, 'PYAIHRNAPLSIIG'),
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
])
def test_zigzag_conversion(s: str, numRows: int, res: str):
    assert Solution().convert(s, numRows) == res