import pytest


# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should
# only have a single space separating the words. Do not include any extra spaces.
class SolutionFast:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = n-1
        ans = ""

        while i >= 0:
            while i > -1 and s[i] == ' ':
                i -= 1

            k = i
            while i > -1 and s[i] != ' ':
                i -= 1

            if k < 0:
                break

            j = i + 1

            while j != k+1:
                ans += s[j]
                j += 1
            ans += " "

        return ans[:-1]


@pytest.mark.parametrize('s, res', [
    ("a", "a"),
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
])
@pytest.mark.parametrize('solution_class', [Solution, SolutionFast])
def test_reverse_words(solution_class, s: str, res: str):
    assert solution_class().reverseWords(s) == res