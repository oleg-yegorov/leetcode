# Definition for a binary tree node.
import pytest

import utility


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionOthers:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        elif l or r:
            return l or r


class SolutionOthersMy:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(node: TreeNode, p: TreeNode, stack: list[TreeNode]):
            if not node:
                return

            if len(stack)>1 and stack[-1] == p:
                return

            if node:
                stack.append(node)
            else:
                return

            path(node.left, p, stack)
            while stack[-1] not in [node, p]:
                stack.pop()

            path(node.right, p, stack)
            while stack[-1] not in [node, p]:
                stack.pop()

        stack1: list[TreeNode] = []
        path(root, p, stack1)

        stack2: list[TreeNode] = []
        path(root, q, stack2)

        for i in range(min(len(stack1), len(stack2))):
            if stack1[i] != stack2[i]:
                return stack1[i-1]
        else:
            return stack1[min(len(stack1), len(stack2))-1]


@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[TreeNode]))
def test_lowest_common_ancestor(solution_class):
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    assert solution_class().lowestCommonAncestor(root, root.left, root.left.right.right) is root.left
    assert solution_class().lowestCommonAncestor(root, root.left, root.right) is root

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution_class().lowestCommonAncestor(root, root, root.right) is root
