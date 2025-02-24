from typing import Optional, List
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self is other:
            return True

        return self.val == other.val and self.left == other.left and self.right == other.right

    def equal_except_for_one_child_nodes(self, other):
        if not other:
            return False

        if self is other:
            return True

        if self.val != other.val:
            return False

        if self.left and self.right and other.left and other.right:
            return (self.left.equal_except_for_one_child_nodes(other.left) and
                    self.right.equal_except_for_one_child_nodes(other.right)) or \
                (self.left.equal_except_for_one_child_nodes(other.right) and
                 self.right.equal_except_for_one_child_nodes(other.left))

        if (self.left is None) != (self.right is None) and (other.left is None) != (other.right is None):
            if self.left and other.left:
                return self.left.equal_except_for_one_child_nodes(other.left)
            elif self.left and other.right:
                return self.left.equal_except_for_one_child_nodes(other.right)
            else:
                return self.right.equal_except_for_one_child_nodes(other.right)

        if not(self.left or self.right or other.left or other.right):
            return True


# Construct binary tree from preorder and postorder traversal
class Solution:

    # У нас есть два представления: preorder, то есть NLR, и postorder, то есть LRN.
    # Сначала реверсируем LRN в NRL просто взяв обход в обратном порядке
    # А потом находим, что для вершин только с листьями выполняется условие: для них в обоих порядках NRL и NLR
    # если листок один, то и вершина и листок идут подряд. А если вершина имеет два листка, то эти три вершины
    # тоже идут подряд, но листки идут в разных порядках. Постепенно строя дерево и удаляю известную информацию из
    # обходов, получаем одну вершину. При этом если у вершины только один листок, определить точно положение (правое или
    # левое) нельзя.
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None

        nodes = [TreeNode(n) for n in preorder]
        postorder.reverse()

        while len(preorder) != 1:
            for i in range(len(preorder) - 2, -1, -1):
                postorder_index = postorder.index(preorder[i])
                if postorder_index + 1 < len(postorder) and preorder[i + 1] == postorder[postorder_index + 1]:
                    nodes[i].left = nodes[i + 1]
                    del nodes[i + 1]
                    del postorder[postorder_index + 1]
                    del preorder[i + 1]
                    break
                if postorder_index + 2 < len(postorder) and i + 2 < len(preorder) and \
                        preorder[i + 2] == postorder[postorder_index + 1] and \
                        preorder[i + 1] == postorder[postorder_index + 2]:
                    nodes[i].left = nodes[i + 1]
                    nodes[i].right = nodes[i + 2]
                    del nodes[i + 1]; del nodes[i + 1]
                    del postorder[postorder_index + 1]; del postorder[postorder_index + 1]
                    del preorder[i + 1]; del preorder[i + 1]
                    break

        return nodes[0]


def test_construct_binary_tree():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]

    tree_node = TreeNode(1, None, None)
    tree_node.left = TreeNode(2, None, None)
    tree_node.right = TreeNode(3, None, None)
    tree_node.left.left = TreeNode(4, None, None)
    tree_node.left.right = TreeNode(5, None, None)
    tree_node.right.left = TreeNode(6, None, None)
    tree_node.right.right = TreeNode(7, None, None)

    res_tree = Solution().constructFromPrePost(preorder, postorder)
    tree_node.equal_except_for_one_child_nodes(res_tree)


def test_construct_binary_tree_from_2():
    preorder = []
    postorder = []

    res_tree = Solution().constructFromPrePost(preorder, postorder)
    assert res_tree is None


def test_construct_binary_tree_from_3():
    preorder = [2, 1, 3]
    postorder = [3, 1, 2]

    tree_node = TreeNode(2, None, None)
    tree_node.left = TreeNode(1, None, None)
    tree_node.left.left = TreeNode(3, None, None)

    res_tree = Solution().constructFromPrePost(preorder, postorder)
    assert res_tree.equal_except_for_one_child_nodes(tree_node)


def test_construct_binary_tree_from_4():
    preorder = [1, 3, 2, 4]
    postorder = [3, 4, 2, 1]

    tree_node = TreeNode(1, None, None)
    tree_node.left = TreeNode(3, None, None)
    tree_node.right = TreeNode(2, None, None)
    tree_node.right.left = TreeNode(4, None, None)

    res_tree = Solution().constructFromPrePost(preorder, postorder)


def test_tree_node_eq():
    tree_node_one = TreeNode(1, None, None)
    assert tree_node_one == tree_node_one

    tree_node_two = TreeNode(1, None, None)
    assert tree_node_one == tree_node_two


def test_tree_node_equal_except_for_one_child():
    tree_node_one = TreeNode(1, None, None)
    tree_node_two = TreeNode(1, None, None)

    assert tree_node_one.equal_except_for_one_child_nodes(tree_node_two)
    assert not tree_node_one.equal_except_for_one_child_nodes(None)

    tree_node_one_child = TreeNode(2, None, None)
    tree_node_one.left = tree_node_one_child

    assert not tree_node_one.equal_except_for_one_child_nodes(tree_node_two)

    tree_node_two_child = TreeNode(2, None, None)
    tree_node_two.left = tree_node_two_child
    assert tree_node_one.equal_except_for_one_child_nodes(tree_node_two)

    tree_node_two.left = None
    tree_node_two.right = tree_node_two_child
    assert tree_node_one.equal_except_for_one_child_nodes(tree_node_two)

    tree_node_one_child2 = TreeNode(3, None, None)
    tree_node_one.right = tree_node_one_child2
    assert not tree_node_one.equal_except_for_one_child_nodes(tree_node_two)

    tree_node_two_child2 = TreeNode(3, None, None)
    tree_node_two.left = tree_node_two_child2
    assert tree_node_one.equal_except_for_one_child_nodes(tree_node_two)
