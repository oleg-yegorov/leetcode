from typing import List

import pytest


# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
# return 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for n in prices:
            profit = max(profit, n - min_price)
            min_price = min(min_price, n)

        return profit


@pytest.mark.parametrize('prices, res', [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(prices: List[int], res: int):
    assert Solution().maxProfit(prices) == res
