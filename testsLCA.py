import unittest
import lowestCommonAncestor
from binarytree import tree, bst, heap, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_empty_tree(self):
        """Test that an empty tree returns None for LCA"""
        root = None
        lca = lowestCommonAncestor.LowestCommonAncestor(root, root, root)
        self.assertEqual(lca.answer, None, f'Incorrect LCA: {lca.answer}. Should be {None}')

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""

        root = tree(height=0)
        lca = lowestCommonAncestor.LowestCommonAncestor(root, root, root)
        self.assertEqual(lca.answer, root, f'Incorrect LCA: {lca.answer}. Should be {root}')

    def test_simple_tree(self):
        """Tests simple binary tree where root is LCA"""

        root = tree(height=1, is_perfect=True)
        lca = lowestCommonAncestor.LowestCommonAncestor(root, root.left, root.right)

        self.assertEqual(lca.answer, root, f'Incorrect LCA: {lca.answer}. Should be {root}')

if __name__ == '__main__':
    unittest.main()
