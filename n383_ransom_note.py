from collections import Counter

import pytest


# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
# magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = Counter(ransomNote)
        magazineCouter = Counter(magazine)

        for key, value in ransomNoteCounter.items():
            if key not in magazineCouter or magazineCouter[key] < value:
                return False

        return True


@pytest.mark.parametrize('ransom_note, magazine, res', [
    ('a', 'b', False),
    ('aa', 'ab', False),
    ('aa', 'aab', True),
])
def test_ransom_note(ransom_note: str, magazine: str, res: bool):
    assert Solution().canConstruct(ransom_note, magazine) == res