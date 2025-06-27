import pytest


# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a
# non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        f = {}
        try:
            for p, word in zip(pattern, s.split(), strict=True):
                if p not in d:
                    d[p] = word
                elif d[p] != word:
                    return False

                if word not in f:
                    f[word] = p
                elif f[word] != p:
                    return False
        except ValueError:
            return False

        return True


@pytest.mark.parametrize('pattern, s, res', [
    ("aaa", "aa aa aa aa", False),
    ('abba', 'dog cat cat dog', True),
    ('abba', 'dog cat cat fish', False),
    ('aaaa', 'dog cat cat dog', False),
])
def test_word_patter(pattern: str, s: str, res: bool):
    assert Solution().wordPattern(pattern, s) == res