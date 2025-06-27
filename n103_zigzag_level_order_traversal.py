from typing import Optional, List

from auxiliary_types import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_nodes = [[root]]
        level_val = [[root.val]]
        reverse = True
        while level_nodes[-1]:
            new_level_val = []
            new_level_nodes = []
            for node in level_nodes[-1]:
                if node.left:
                    new_level_val.append(node.left.val)
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_val.append(node.right.val)
                    new_level_nodes.append(node.right)
            level_val.append(list(reversed(new_level_val)) if reverse else new_level_val)
            reverse = not reverse
            level_nodes.append(new_level_nodes)
        return level_val[:-1]


def test_level_order():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrder(root) == [[3], [20,9], [15, 7]]
