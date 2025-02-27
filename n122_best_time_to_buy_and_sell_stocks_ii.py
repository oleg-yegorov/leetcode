from typing import List

import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = sell_price = prices[0]
        profit = 0

        for n in prices:
            if n < sell_price:
                profit += sell_price - buy_price
                buy_price = sell_price = n
            else:
                sell_price = n

        profit += sell_price - buy_price
        return profit


@pytest.mark.parametrize('prices, res', [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0 )
])
def test_max_profit_ii(prices: List[int], res: int):
    assert Solution().maxProfit(prices) == res
