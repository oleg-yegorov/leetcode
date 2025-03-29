from typing import List

import pytest

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
class Solution:
    def valid_digits(self, block):
        s = set()
        for d in block:
            if d == '.':
                continue

            if d in s:
                return False
            else:
                s.add(d)
        else:
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.valid_digits(row):
                return False

        for i in range(9):
            if not self.valid_digits(row[i] for row in board):
                return False

        for i in range(3):
            for j in range(3):
                block = (col for row in board[i * 3:i * 3 + 3] for col in row[j * 3:j * 3 + 3])
                if not self.valid_digits(block):
                    return False

        return True


@pytest.mark.parametrize('board, valid', [
    ([["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]], True),
    ([["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]], False)
])
def test_is_valid_sudoku(board: List[List[str]], valid: bool):
    assert Solution().isValidSudoku(board) == valid


