from collections import Counter

import pytest


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


@pytest.mark.parametrize('s, t, res', [
    ('anagram', 'nagaram', True),
    ('rat', 'car', False),
])
def test_is_anagram(s, t, res):
    assert Solution().isAnagram(s, t) == res