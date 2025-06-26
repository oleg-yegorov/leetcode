import pytest

import utility


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
# and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while not s[left_ptr].isalnum():
                left_ptr += 1
                if left_ptr > right_ptr:
                    return True

            while not s[right_ptr].isalnum():
                right_ptr -= 1
                if right_ptr < left_ptr:
                    return True

            if s[left_ptr].capitalize() != s[right_ptr].capitalize():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True


class SolutionFilterMap:
    def isPalindrome(self, s: str) -> bool:
        filtered = filter(lambda ch: ch.isalnum(), s)
        filtered_cat = map(lambda ch: ch.capitalize(), filtered)
        filtered_cat_list = list(filtered_cat)
        filtered_cat_list_reversed = list(reversed(filtered_cat_list))

        return filtered_cat_list == filtered_cat_list_reversed


@pytest.mark.parametrize('s, res', [
    ("!!!", True),
    ("0P", False),
    (".,", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("  ", True),
])
@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[]))
def test_is_palindrome(solution_class, s: str, res: bool):
    assert solution_class().isPalindrome(s) == res