import pytest


# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        i = 0
        while i < n - m + 1:
            jump = 0
            for j in range(m):
                if haystack[j + i] != needle[j]:
                    break
                else:
                    jump += 1
            else:
                return i

            # i += jump if jump else 1
            i += 1

        return -1


@pytest.mark.parametrize('haystack, needle, res', [
    ("mississippi", "issip", 4),
    ("a", "b", -1),
    ("a", "a", 0),
    ('finfind', 'find', 3),
    ('find', 'nd', 2),
    ('sadbutsad', 'sad', 0),
    ('leetcode', 'leeto', -1),
])
def test_finst_occurance(haystack: str, needle: str, res: int):
    assert Solution().strStr(haystack, needle) == res
