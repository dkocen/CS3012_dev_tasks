import unittest
import lowestCommonAncestor
from binarytree import tree, bst, heap


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_empty_tree(self):
        """Test that an empty tree returns None for LCA"""

        data = [None]
        node1_val = None
        node2_val = None
        tree = bt.BinaryTree(data)
        lca = lowestCommonAncestor.LowestCommonAncestor(tree.root, node1_val, node2_val)

        self.assertEqual(tree.inorder, [None], f'Incorrect tree: {tree.inorder}. Should be {None}')
        self.assertEqual(lca.answer.key, None, f'Incorrect LCA: {lca.answer}. Should be {None}')

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""
        tree = tree(height=)

        data = [-1]
        node1_val = 0
        node2_val = 0
        tree = bt.BinaryTree(data)
        lca = lowestCommonAncestor.LowestCommonAncestor(tree.root, node1_val, node2_val)

        self.assertEqual(tree.inorder, [0], f'Incorrect tree: {tree.inorder}. Should be {[0]}')
        self.assertEqual(lca.answer.key, 0, f'Incorrect LCA: {lca.answer}. Should be {0}')

    def test_simple_tree(self):
        """Tests simple binary tree where root is LCA"""

        data = [-1, 0, 0]
        node1_val = 1
        node2_val = 2
        tree = bt.BinaryTree(data)
        lca = lowestCommonAncestor.LowestCommonAncestor(tree.root, node1_val, node2_val)

        self.assertEqual(tree.inorder, [1, 0, 2], f'Incorrect tree: {tree.inorder}. Should be [1, 0, 2]')
        self.assertEqual(lca.answer.key, 0, f'Incorrect LCA: {lca.answer}. Should be {0}')

if __name__ == '__main__':
    unittest.main()
