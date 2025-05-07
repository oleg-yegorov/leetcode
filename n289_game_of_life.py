from typing import List

import pytest


class Solution:
    def neibs(self, board: List[List[int]], i: int, j: int) -> int:
        i_l = max(0, i-1)
        i_h = min(len(board), i+2)
        j_l = max(0, j-1)
        j_h = min(len(board[0]), j+2)

        neibs = sum(1 for row in board[i_l:i_h] for el in row[j_l:j_h] if el in [1,2])
        return neibs-1 if board[i][j] == 1 else neibs

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neibs = self.neibs(board, i, j)
                if board[i][j] == 0 and neibs == 3:
                    board[i][j] = 3
                if board[i][j] == 1 and (neibs < 2 or neibs > 3):
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0


@pytest.mark.parametrize('board, tobe', [
    ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]),
    ([[1,1],[1,0]], [[1,1],[1,1]]),
    ([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
])
def test_game_of_life(board: List[List[int]], tobe: List[List[int]]):
    Solution().gameOfLife(board)
    assert board == tobe

# 0 1 0    ->    0 0 0
# 0 0 1    ->    1 0 1
# 1 1 1    ->    0 1 1
# 0 0 0    ->    0 1 0


# Neib      Prev    ToBe
# 0-1, 4-8  0       0
# 0-1, 4-8  1       0

# 2         0       0
# 2         1       1

# 3         0       1
# 3         1       1

# Не изменяется
# 0-1, 4-8  0       0
# 2         0       0
# 2         1       1
# 3         1       1

# Изменяется
# 0-1, 4-8  1       0
# 3         0       1
