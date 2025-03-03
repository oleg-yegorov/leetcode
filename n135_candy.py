from typing import List

import pytest


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        candies = [0] * n

        i = 1
        candies[0] = 1
        while i < n:
            prev_rat = ratings[i - 1]
            cur_rat = ratings[i]

            if prev_rat == cur_rat:
                candies[i] = 1
                i += 1
            elif prev_rat < cur_rat:
                candies[i] = candies[i-1] + 1
                i += 1
            else:
                count = 1
                j = i + 1
                while j < n and ratings[j] < ratings[j-1]:
                    count += 1
                    j += 1

                if candies[i - 1] < count + 1:
                    candies[i - 1] = count + 1

                j = i
                i += count
                while count:
                    candies[j] = count
                    count -= 1
                    j += 1

        return sum(candies)


@pytest.mark.parametrize('ratings, res', [
    ([5, 4, 3, 2, 1, 0], 21),
    ([1,6,10,8,7,3,2], 18),
    ([1, 2, 4, 4, 3, 0], 12),
    ([1, 3, 4, 5, 2], 11),
    ([29,51,87,87,72,12], 12),
    ([1, 0, 2], 5),
    ([1, 2, 2], 4)
])
def test_candy(ratings: List[int], res: int):
    assert Solution().candy(ratings) == res
