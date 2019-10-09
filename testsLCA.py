import unittest
import lowestCommonAncestor as LCA
from binarytree import tree, build, Node
import networkx as nx


class ThreeNode:
    """Used for making a non-binary tree"""
    def __init__(self, value, left=None, center=None, right=None):
        self.value = value
        self.left = left
        self.center = center
        self.right = right


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

    def test_straight_left(self):
        """Tests a all left node tree (essentially a linked list)"""
        values = [0, 1, None, 2, None, None, None, 3, None, None, None, None, None, None, None]

        root = build(values)
        lca = LCA.findLCA(root, root.left.left.left, root.left.left)

        self.assertEqual(lca, root.left.left, f'Incorrect LCA {lca}. Should be {root.left.left}')

    def test_straight_right(self):
        """Tests a all right node tree"""
        values = [0, None, 1, None, None, None, 2, None, None, None, None, None, None, None, 3]

        root = build(values)
        lca = LCA.findLCA(root, root.right.right.right, root.right.right)

        self.assertEqual(lca, root.right.right, f'Incorrect LCA {lca}. Should be {root.right.right}')

    def test_null_leaf(self):
        """Tests tree where one node is None. Should return non-None leaf"""
        values = [0, 1, 2, 3, None]

        root = build(values)
        lca = LCA.findLCA(root, root.left.left, root.left.right)

        self.assertEqual(lca, root.left.left, f'Incorrect LCA {lca}. Should be {root.left.left}')

    def test_balanced_tree(self):
        """Tests a balanced tree based on generated list of 100 random numbers online"""
        values = [10, 12, 14, 24, 39, 50, 54, 62, 67, 92, 134, 153, 161, 162, 167, 171, 172, 173, 191, 193, 197, 205, 206, 208, 210, 211, 222, 239, 240, 246, 249, 253, 263, 270, 286, 299, 303, 305, 308, 316, 319, 325, 344, 349, 350, 353, 363, 365, 371, 395, 414, 437, 453, 459, 463, 489, 500, 503, 512, 514, 515, 516, 518, 530, 553, 558, 573, 574, 578, 586, 590, 602, 607, 618, 636, 638, 647, 676, 690, 691, 716, 761, 767, 798, 811, 815, 836, 843, 849, 867, 882, 903, 919, 921, 943, 948, 958, 959, 980, 997]

        root = build(values)
        lca1 = LCA.findLCA(root, root.left.left.left.left.right, root.right.left.left.right.left.left)
        lca2 = LCA.findLCA(root, root.right.right.left.right.right, root.right.right.right.left.left)
        lca3 = LCA.findLCA(root, root.left.right.right, root)
        lca4 = LCA.findLCA(root, root.right.left.right.right, root.right.left)

        self.assertEqual(lca1, root, f'Incorrect LCA {lca1}. Should be {root}')
        self.assertEqual(lca2, root.right.right, f'Incorrect LCA {lca2}. Should be {root}')
        self.assertEqual(lca3, root, f'Incorrect LCA {lca3}. Should be {root}')
        self.assertEqual(lca4, root.right.left, f'Incorrect LCA {lca4}. Should be {root.right.left}')

    def test_unbalanced_tree(self):
        """Tests an unbalanced tree based on random binary tree generator online"""
        root = Node(67)
        root.left = Node(11)
        root.right = Node(82)
        root.left.left = Node(4)
        root.left.right = Node(60)
        root.left.right.left = Node(52)
        root.left.right.left.left = Node(23)
        root.left.right.left.left.right = Node(38)
        root.left.right.left.left.left = Node(74)
        root.left.right.left.left.right.left = Node(46)

        lca1 = LCA.findLCA(root, root.right, root.left.right.left.left)
        lca2 = LCA.findLCA(root, root.left.left, root.left.right.left.left)
        lca3 = LCA.findLCA(root, root.left.right.left.left.right, root.left.right.left.left.left)

        self.assertEqual(lca1, root, f'Incorrect LCA {lca1}. Should be {root}')
        self.assertEqual(lca2, root.left, f'Incorrect LCA {lca2}. Should be {root.left}')
        self.assertEqual(lca3, root.left.right.left.left, f'Incorrect LCA {lca3}. Should be {root.left.right.left.left}')

    def test_lca_multiple_nodes(self):
        root = Node(67)
        root.left = Node(11)
        root.right = Node(82)
        root.left.left = Node(4)
        root.left.right = Node(60)
        root.left.right.left = Node(52)
        root.left.right.left.left = Node(23)
        root.left.right.left.left.right = Node(38)
        root.left.right.left.left.left = Node(74)
        root.left.right.left.left.right.left = Node(46)

        lca = LCA.findLCA(root, root.left.left, root.right, root.left.right.left.left)

        self.assertEqual(lca, root, f'Incorrect LCA {lca}. Should be {root}')

    def test_non_binary_tree(self):
        """Tests a simple non_binary tree (from slide 3 of LCA slides)"""

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.left.left = Node(6)
        root.right.left = Node(5)
        root.right.left.left = Node(7)
        root.right.left.right = Node(8)
        root.right.left.left.left = ThreeNode(10)
        root.right.left.left.left.left = Node(9)
        root.right.left.left.left.center = Node(13)
        root.right.left.left.left.right = Node(11)
        root.right.left.left.left.right.left = Node(12)

        lca = LCA.findLCA(root, root.right.left.right, root.right.left.left.left.left)

        self.assertEqual(lca, root.right.left, f'Incorrect LCA {lca1}. Should be {root.right.left}')

    def test_simple_dag(self):
        """Tests a basic DAG"""
        graph = [(0, 1), [0, 2], [1, 3], [2, 3], [1, 4]]
        lca1 = LCA.findLCA(graph, 1, 2)
        lca2 = LCA.findLCA(graph, 1, 3)
        lca3 = LCA.findLCA(graph, 3, 4)

        self.assertEqual(lca1, 0, f'Incorrect LCA {lca1}. Should be {0}')
        self.assertEqual(lca2, 1, f'Incorrect LCA {lca2}. Should be {1}')
        self.assertEqual(lca3, 1, f'Incorrect LCA {lca3}. Should be {1}')

if __name__ == '__main__':
    unittest.main()
