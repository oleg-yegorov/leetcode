from collections import Counter

import pytest


# Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        left = max_len = 0

        for right in range(len(s)):
            c = s[right]
            chars[c] += 1

            while chars[c] > 1:
                chars[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

@pytest.mark.parametrize('s, res', [
    ("", 0),
    ("a", 1),
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_longest_substring_without_repeating_characters(s: str, res: int):
    assert Solution().lengthOfLongestSubstring(s) == res