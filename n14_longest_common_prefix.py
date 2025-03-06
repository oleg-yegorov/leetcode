from typing import List

import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        for strr in strs:
            min_length = min(len(strr), min_length)

        for i in range(min_length):
            for strr in strs:
                if strs[0][i] != strr[i]:
                    return strs[0][:i]

        return strs[0][:min_length]


@pytest.mark.parametrize('strs, res', [
    (["flower", "flow", "flow_flight"], 'flow'),
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], ""),
])
def test_longest_prefix(strs: List[str], res: str):
    assert Solution().longestCommonPrefix(strs) == res

