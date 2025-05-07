import pytest
from typing import List
from collections import Counter, defaultdict

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = []
        str_list = []
        for str in strs:
            counter = Counter(str)
            for i, counter_list_el in enumerate(counter_list):
                if len(str) == len(str_list[i][0]) and counter_list_el == counter:
                    str_list[i].append(str)
                    break
            else:
                counter_list.append(counter)
                str_list.append([str])

        return str_list

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        str_list = []
        for _str in strs:
            sorted_str = ''.join(sorted(_str))
            try:
                ind = sorted_list.index(sorted_str)
                str_list[ind].append(_str)
            except ValueError:
                sorted_list.append(sorted_str)
                str_list.append([_str])

        return str_list

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for _str in strs:
            sorted_str = ''.join(sorted(_str))
            d[sorted_str].append(_str)

        return list(d.values())

@pytest.mark.parametrize('strs, res', [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([""],  [[""]]),
    (["a"], [["a"]]),
])
def test_group_anagrams(strs: List[str], res: List[List[int]]):
    assert Solution().groupAnagrams3(strs) == res