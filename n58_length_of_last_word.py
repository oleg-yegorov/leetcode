import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        i = n - 1
        while s[i] == " ":
            i -= 1

        j = i
        while j >= 0 and s[j] != " ":
            j -= 1

        return i - j


@pytest.mark.parametrize('s, res', [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6)
])
def test_length_of_last_word(s: str, res: int):
    assert Solution().lengthOfLastWord(s) == res
