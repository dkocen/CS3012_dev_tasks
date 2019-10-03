import unittest
import lowestCommonAncestor
from binarytree import tree, bst, heap, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_empty_tree(self):
        """Test that an empty tree returns None for LCA"""
        root = None
        lca = lowestCommonAncestor.LowestCommonAncestor(root, node1_val, node2_val)

        self.assertEqual(root.inorder, [None], f'Incorrect tree: {tree.inorder}. Should be {None}')
        self.assertEqual(lca.answer, None, f'Incorrect LCA: {lca.answer}. Should be {None}')

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""

        root = tree(height=0)
        lca = lowestCommonAncestor.LowestCommonAncestor(root, root, root)

        self.assertEqual(str(list(root)), str([Node(0)]), f'Incorrect tree: {root.levelorder}. Should be {[Node(0)]}')
        self.assertEqual(lca.answer, Node(0), f'Incorrect LCA: {lca.answer}. Should be {Node(0)}')

    def test_simple_tree(self):
        """Tests simple binary tree where root is LCA"""

        root = tree(height=1, is_perfect=True)

        data = [-1, 0, 0]
        node1_val = 1
        node2_val = 2
        tree = bt.BinaryTree(data)
        lca = lowestCommonAncestor.LowestCommonAncestor(tree.root, node1_val, node2_val)

        self.assertEqual(tree.inorder, [1, 0, 2], f'Incorrect tree: {tree.inorder}. Should be [1, 0, 2]')
        self.assertEqual(lca.answer.key, 0, f'Incorrect LCA: {lca.answer}. Should be {0}')

if __name__ == '__main__':
    unittest.main()
