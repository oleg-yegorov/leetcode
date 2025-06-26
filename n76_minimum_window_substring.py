from collections import Counter

import pytest


# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window. If there is no such substring, return the
# empty string "".
# The testcases will be generated such that the answer is unique.
class Solution:
    def compCounters(self, c1: Counter, c2: Counter) -> bool:
        for k in c1:
            if k not in c2 or c1[k] > c2[k]:
                return False
        else:
            return True

    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        r = Counter()
        left = 0
        min_length = float("inf")
        min_str = ""
        for right in range(len(s)):
            p = s[right]
            if p in c:
                r[p] += 1

                while self.compCounters(c, r):
                    if min_length > right - left + 1:
                        min_length = right - left + 1
                        min_str = s[left:right + 1]

                    if s[left] in r:
                        r[s[left]] -= 1
                    left += 1

        return min_str


@pytest.mark.parametrize('s, t, res', [
    ("aaaaaaaaaaaabbbbbcdd", "abcdd", "abbbbbcdd"),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", "")
])
def test_min_window(s, t, res):
    assert Solution().minWindow(s, t) == res

