from typing import List

import pytest


# Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 0 1 .. n
        # .
        # m

        m = len(matrix)
        n = len(matrix[0])
        n0 = 0
        n1 = n
        m0 = 0
        m1 = m

        ans = []
        while n0 < n1 and m0 < m1:
            ans.extend(matrix[m0][n0:n1])
            m0 += 1

            ans.extend(row[n1-1] for row in matrix[m0: m1])
            n1 -= 1

            if n0 < n1 and m0 < m1:
                if n0 - 1 >= 0:
                    ans.extend(matrix[m1-1][n1-1:n0-1:-1])
                else:
                    ans.extend(matrix[m1 - 1][n1 - 1::-1])
                m1 -= 1

                ans.extend(row[n0] for row in matrix[m1-1:m0-1:-1])
                n0 += 1

        return ans


@pytest.mark.parametrize('matrix, ans', [
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]], [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]),
    ([[7],[9],[6]], [7, 9, 6]),
    ([[6,9,7]], [6, 9, 7]),
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ([[1]], [1]),
    ([[3],[2]], [3, 2]),
])
def test_spiral_matrix(matrix: List[List[int]], ans: List[int]):
    assert Solution().spiralOrder(matrix) == ans
