from typing import Optional

import pytest

import utility


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionOthers:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Решение из интернета. Если левое и правое направление совпадают по длине, то дерево полное дерево сбалансированно,
        # (максимальное количество вершин), и можно посчитать количество его вершин по формуле 2**n. Если оно не
        # сбалансировано, то смотрим, сбалансированы ли левое и правое поддеревья, и так рекурсивно, пока не найдем
        # такие.
        if not root:
            return 0

        def l_height(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + l_height(node.left)

        def r_height(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + r_height(node.right)

        l, r = l_height(root), r_height(root)
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 2**l - 1


class SolutionOthers:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Это мое решение. Тут я вычисляю высоту дерева и потом нахожу, где заканчивается последний ряд методом
        # бинарного поиска
        if not root:
            return 0

        height = 1
        ptr = root
        while ptr := ptr.left:
            height += 1

        if height == 1:
            return 1

        last_level_nodes = pow(2, height-1) - 1

        miss = set()
        hit = set()

        start = 0
        end = last_level_nodes
        first_1 = False
        while True:
            arrow = (end - start) // 2 + start

            if end - start == 1:
                if not first_1:
                    first_1 = True
                else:
                    arrow += 1

            ptr = root
            for i in format(arrow, f'0{height-1}b'):
                ptr = ptr.left if i == '0' else ptr.right
            if not ptr:
                miss.add(arrow)
                if arrow-1 in hit:
                    return arrow + last_level_nodes
                else:
                    end = arrow
            else:
                hit.add(arrow)
                if arrow + 1 in miss or arrow == last_level_nodes:
                    return arrow + last_level_nodes + 1
                else:
                    start = arrow


@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[TreeNode]))
def test_count_complete_binary_tree_nodes(solution_class):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert solution_class().countNodes(root) == 3

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    assert solution_class().countNodes(root) == 6

    assert solution_class().countNodes(None) == 0

    assert solution_class().countNodes(TreeNode(1)) == 1
