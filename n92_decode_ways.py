from typing import Tuple

import pytest

import utility


# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following
# mapping: "1" -> 'A' ...  "26" -> 'Z'
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot
# be decoded in any valid way, return 0.
class SolutionRec:
    # Рекурсия. Доходим до последнего символа. Если на данных момент все без ошибок - возвращаем 1. То есть количество
    # возможных комбинаций на данном шаге. Потом идем наверх и складываем их. Сумма отображает следующее: сколько
    # будет правильных комбинаций оставшейся справа строки. Для самого левого символа это число будет равно решению.
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

class SolutionSeqs:
    # Надо разбить строку на отрезки, в которых есть последовательность 1 или 2. Тогда каждый отрезок будет
    # отражать столько комбинаций, сколько отображает функция Фибоначчи. Далее нужно перемножить все эти интервалы.
    # Крайние случаи: перед 0 должна стоять 1 или 2.
    # Количество комбинация это функция Фибоначчи, потому что складывается количество комбинаций на предыдущем шаге
    # (возможна буква а или б) и комбинации два шага назад (возможна буква из двух символов).
    def numDecodings(self, s: str) -> int:
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

    def fib(self, n):
        if n in [0, 1]:
            return 1

        first = 1
        second = 1

        for _ in range(n - 1):
            second = first + second
            first = second - first

        return second


class SolutionDP:
    # Динамичное программирование. Если текущее однозначное число подходит, то добавляем его варианты к предыдущему.
    # Если текущее число двузначное, то добавляем его варианты к следующему результату
    def numDecodings(self, s: str) -> int:
        res = [0] * (len(s) + 1)
        res[0] = 1

        for i in range(len(s)):
            if 1 <= int(s[i]) <= 9:
                res[i + 1] += res[i]

            if i + 1 < len(s) and 10 <= int(s[i]) * 10 + int(s[i+1]) <= 26:
                res[i + 2] += res[i]

        return res[-1]


class SolutionDPwithoutArray:
    # Так как весь массив промежуточных значений не нужен, то храним только нужные: предыдущее, текущее и следующее
    def numDecodings(self, s: str) -> int:
        prev = 0
        cur = 1
        next = 0

        for i in range(len(s)):
            prev = cur
            cur = next
            next = 0

            if 1 <= int(s[i]) <= 9:
                cur += prev

            if i + 1 < len(s) and 10 <= int(s[i]) * 10 + int(s[i+1]) <= 26:
                next += prev

        return cur


@pytest.mark.parametrize('s, ret', [
    ("11106", 2),
    ("00", 0),
    ("301", 0),
    ("227", 2),
    ("111111111111111111111111111111111111111111111", 1836311903),
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("100", 0)
])
@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[SolutionRec]))
def test_decode_ways(solution_class, s, ret):
    assert(solution_class().numDecodings(s) == ret)
