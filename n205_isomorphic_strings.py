import pytest
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        c = {}
        for i, j in zip(s, t):
            if i not in d:
                d[i] = j
            elif d[i] != j:
                return False

            if j not in c:
                c[j] = i
            elif c[j] != i:
                return False

        return True


@pytest.mark.parametrize('s, t, res', [
    ('egg', 'add', True),
    ('foo', 'bar', False),
    ('paper', 'title', True),
    ("badc", "baba", False),
])
def test_is_isomorphic(s: str, t: str, res: bool):
    Solution().isIsomorphic(s, t) == res