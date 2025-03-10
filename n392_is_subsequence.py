import pytest


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (i.e.,
# "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_it = 0
        t_it = 0

        if not(s):
            return True

        while t_it < len(t):
            if s[s_it] == t[t_it]:
                s_it += 1
                if s_it == len(s):
                    return True

            t_it += 1

        return False


@pytest.mark.parametrize('s, t, res', [
    ('b', 'abc', True),
    ('a', '', False),
    ('', 'ahbgdc', True),
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False)
])
def test_is_subsequence(s: str, t: str, res: bool):
    assert Solution().isSubsequence(s, t) == res