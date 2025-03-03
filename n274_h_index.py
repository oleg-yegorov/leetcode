from typing import List


class Solution:
    def hIndexNLogn(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        if citations[n - 1] == 0:
            return 0

        for i in range(n):
            if citations[i] >= n - i:
                return n - i;

        return

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        count = [0] * n
        for v in citations:
            if v > n:
                count[-1] += 1
            elif v > 0:
                count[v - 1] += 1

        sum = 0
        for i in range(n - 1, -1, -1):
            sum += count[i]
            if i + 1 <= sum:
                return i + 1
        else:
            return 0