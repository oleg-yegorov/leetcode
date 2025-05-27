class Solution:
    def calculate(self, s: str) -> int:
        # There are only addition and subtraction. So, you can have a stack of "minus/plus" values for each
        # bracket-ranged numbers and perform operation on a fly.
        # "1 + 1"
        # " 2-1 + 2 "
        # "(1+(4+5+2)-3)+(6+8)"

        # Open-bracket - push value, close-bracket - pop value
        s = s.replace(" ", '')
        if s[0] != '-':
            s = '+' + s

        formatted_s = ""
        for i in range(len(s)):
            formatted_s += s[i]
            if s[i] == '(' and s[i + 1] != '-':
                formatted_s += "+"
        formatted_s += " "

        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        stack: list[bool] = [True]

        nmb = res = 0
        nmb_set = False
        for i in formatted_s:
            if nmb_set and i not in digits:
                res = res + nmb if stack[-1] else res - nmb
                stack.pop()
                nmb = 0
                nmb_set = False

            if i == ' ':
                continue
            elif i == '-':
                stack.append(not stack[-1])
            elif i == '+':
                stack.append(stack[-1])
            elif i in digits:
                nmb = 10 * nmb + digits[i]
                nmb_set = True
            elif i == '(':
                continue
            elif i == ')':
                stack.pop()

        return res


def test_basic_calculator():
    assert Solution().calculate("-( -2)+4") == 6
    assert Solution().calculate("(7)-(0)+(4)") == 11
    assert Solution().calculate("2147483647") == 2147483647
    assert Solution().calculate("1 + 1") == 2
    assert Solution().calculate(" 2-1 + 2 ") == 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
