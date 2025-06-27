from typing import List

import pytest


def get_next_land(grid: List[List[str]]):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == '1':
                return y, x
    return -1, -1


class SolutionOutline:
    # Обход острова по контуру.
    def get_contur(self, grid: List[List[str]], y: int, x: int):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        c = get_next_land()


class SolutionRec:
    # Рекурсивный обход нашего графа. Ищем в четырех валидных направлениях.

    @staticmethod
    def remove_island(y: int, x: int, grid: List[List[str]]):
        grid[y][x] = '0'

        if y-1 >= 0 and grid[y-1][x] == '1':
            SolutionRec.remove_island(y-1, x, grid)
        if x-1 >= 0 and grid[y][x-1] == '1':
            SolutionRec.remove_island(y, x-1, grid)
        if y+1 < len(grid) and grid[y+1][x] == '1':
            SolutionRec.remove_island(y+1, x, grid)
        if x+1 < len(grid[y]) and grid[y][x+1] == '1':
            SolutionRec.remove_island(y, x+1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        while (c := get_next_land(grid)) != (-1, -1):
            res += 1
            SolutionRec().remove_island(c[0], c[1], grid)

        return res


@pytest.mark.parametrize('solution_class', [SolutionRec])
def test_num_of_islands(solution_class):
    grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"],
    ]
    assert solution_class().numIslands(grid) == 1

    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert solution_class().numIslands(grid) == 0

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution_class().numIslands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution_class().numIslands(grid) == 3

    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"],
    ]
    assert solution_class().numIslands(grid) == 2
