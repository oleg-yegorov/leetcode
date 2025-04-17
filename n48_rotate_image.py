from typing import List

import pytest


# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.
class Solution:
    @staticmethod
    def rotate_diag(matrix: List[List[int]]):
        n = len(matrix)
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    @staticmethod
    def mirror_vert(matrix: List[List[int]]):
        n = len(matrix)
        for row in matrix:
            for i in range(0, n // 2):
                row[i], row[n-i-1] = row[n-i-1], row[i]

    def rotate(self, matrix: List[List[int]]) -> None:
        Solution().rotate_diag(matrix)
        Solution().mirror_vert(matrix)


@pytest.mark.parametrize('matrix, output', [
    ([1], [1]),
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
])
def test_rotate(matrix: List[List[int]], output: List[List[int]]):
    Solution().rotate(matrix)
    assert matrix == output
