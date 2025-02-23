from typing import Tuple

import pytest


# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following
# mapping: "1" -> 'A' ...  "26" -> 'Z'
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot
# be decoded in any valid way, return 0.
class Solution:

    def numDecodings(self, s: str) -> int:
        if not s:
            return 1

        forks = 0
        if len(s) > 0 and 1 <= int(s[0]) <= 9:
            if len(s) > 1 and int(s[1]) == 0:
                forks += self.numDecodings(s[2:])
            else:
                forks += self.numDecodings(s[1:])

                if len(s) > 1 and 1 <= int(s[0]) * 10 + int(s[1]) <= 26:
                    forks += self.numDecodings(s[2:])

        return forks

    def fib(self, n):
        if n in [0, 1]:
            return 1

        first = 1
        second = 1

        for _ in range(n - 1):
            second = first + second
            first = second - first

        return second

    # Надо разбить строку на отрезки, в которых есть последовательность 1 или 2. Тогда каждый отрезок будет
    # отражать столько комбинаций, сколько отображает функция Фибоначчи. Далее нужно перемножить все эти интервалы.
    # Крайние случаи: перед 0 должна стоять 1 или 2.
    def numDecodingsSeqs(self, s: str) -> int:
        ind = 0
        mult = 1

        while ind < len(s):
            if s[ind] == '0':
                return 0

            while ind < len(s) and s[ind] not in ['1', '2']:
                if s[ind] == '0' and s[ind - 1] not in ['1', '2']:
                    return 0
                ind += 1

            int_len = 0
            while ind < len(s) and s[ind] in ['1', '2']:
                ind += 1
                int_len += 1

            if ind == len(s):
                mult *= self.fib(int_len)
            elif s[ind] == '0':
                mult *= self.fib(int_len - 1)
            elif s[ind - 1] == '2' and s[ind] in ['7', '8', '9']:
                mult *= self.fib(int_len)
            else:
                mult *= self.fib(int_len + 1)

            ind += 1

        return mult


@pytest.mark.parametrize('s, ret', [
    ("00", 0),
    ("301", 0),
    ("227", 2),
    ("111111111111111111111111111111111111111111111", 1836311903),
    ("11106", 2),
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("100", 0)
])
def test_decode_ways(s, ret):
    assert(Solution().numDecodingsSeqs(s) == ret)
