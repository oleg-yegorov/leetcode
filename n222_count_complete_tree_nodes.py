from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
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


def test_count_complete_binary_tree_nodes():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert Solution().countNodes(root) == 3

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    assert Solution().countNodes(root) == 6

    assert Solution().countNodes(None) == 0

    assert Solution().countNodes(TreeNode(1)) == 1
