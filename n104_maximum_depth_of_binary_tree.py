from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_rec(self, root: Optional[TreeNode]) -> int:
        # recursive
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        # Breadth First Search
        nodes = [root]
        childs = []

        i = 0
        while nodes:
            i += 1
            for node in nodes:
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            nodes = childs
            childs = []

        return i

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Depth First Search

        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return max_depth




def test_max_depth_of_binary_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().maxDepth(root) == 3
