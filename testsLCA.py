import unittest
import lowestCommonAncestor as lca
import binaryTree.py as bt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_empty_tree(self):
        """Test that an empty tree returns None for LCA"""

        data = None
        node1_val = None
        node2_val = None
        root = bt.construct_bt(data)
        result = lca.lowest_common_ancestor(root, node1_val, node2_val)

        self.assertEqual(result.value, None)

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""

        data = [0]
        node1_val = 0
        node2_val = 0
        root = lca.construct_bt(data)
        result = lca.lowest_common_ancestor(root, node1_val, node2_val)

        self.assertEqual(result.value, 0)

    def test_simple_tree(self):
        """Tests simple binary tree where root is LCA"""

        data = [0,1,2]
        node1_val = 1
        node2_val = 2
        root = lca.construct_bt(data)
        result = lca.lowest_common_ancestor(root, node1_val, node2_val)

        self.assertEqual(result.value, 0)

if __name__ == '__main__':
    unittest.main()
