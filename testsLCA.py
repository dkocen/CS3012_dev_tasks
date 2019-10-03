import unittest
import lowestCommonAncestor as LCA
from binarytree import tree, bst, heap, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_empty_tree(self):
        """Test that an empty tree returns None for LCA"""
        root = None
        lca = LCA.findLCA(root, root, root)
        self.assertEqual(lca, None, f'Incorrect LCA: {lca}. Should be {None}')

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""

        root = tree(height=0)
        lca = LCA.findLCA(root, root, root)
        self.assertEqual(lca, root, f'Incorrect LCA: {lca}. Should be {root}')

    def test_simple_tree(self):
        """Tests simple binary tree where root is LCA"""

        root = tree(height=1, is_perfect=True)
        lca = LCA.findLCA(root, root.left, root.right)

        self.assertEqual(lca, root, f'Incorrect LCA: {lca}. Should be {root}')

if __name__ == '__main__':
    unittest.main()
