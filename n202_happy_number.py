# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
class Solution:
    def squared_digits(self, n) -> int:
        str_n = str(n)
        return sum(int(i)*int(i) for i in str_n)

    def isHappy(self, n: int) -> bool:
        squared_digits = {n}

        while True:
            sq = self.squared_digits(n)
            if sq == 1:
                return True
            elif sq in squared_digits:
                return False
            squared_digits.add(sq)
            n = sq


def test_is_happy():
    assert Solution().isHappy(1)
    assert Solution().isHappy(19)  # 19, 82, 68, 100, 1.
    assert not Solution().isHappy(2)  # 2, 4, 16, 37, 58, 89, 145, 42, 20, 4 ....
