from typing import List

import pytest


# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        null_first_row = 0 in matrix[0]
        null_first_col = 0 in (matrix[i][0] for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i] = [0] * m

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0

        if null_first_row:
            matrix[0] = [0] * m

        if null_first_col:
            for j in range(n):
                matrix[j][0] = 0


@pytest.mark.parametrize('matrix, res', [
    ([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]], [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]),
    ([[1,0,3]], [[0,0,0]]),
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
])
def test_set_zeroes(matrix: List[List[int]], res: List[List[int]]):
    Solution().setZeroes(matrix)
    assert matrix == res
