import unittest
import lowestCommonAncestor as LCA
from binarytree import tree, build, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Just a test to make sure it works. Should always pass"""

        self.assertEqual(True, True)

    def test_empty_tree(self):
        """Test that an empty tree returns False for LCA. Logic is considering empty tree to not be a tree"""

        root = None
        lca = LCA.findLCA(root, root, root)
        self.assertEqual(lca, False, f'Incorrect LCA: {lca}. Should be {False}')

    def test_single_node(self):
        """Test that single node tree returns single node for LCA"""

        root = tree(height=0)
        lca1 = LCA.findLCA(root, root, root)
        lca2 = LCA.findLCA(root, root.left, root.right)

        self.assertEqual(lca1, root, f'Incorrect LCA: {lca1}. Should be {root}')
        self.assertEqual(lca2, None, f'Incorrect LCA: {lca2}. Should be {None}')

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

        values = [10, 12, 14, 24, 39, 50, 54, 62, 67, 92, 134, 153, 161, 162, 167, 171, 172, 173, 191, 193, 197, 205,
                  206, 208, 210, 211, 222, 239, 240, 246, 249, 253, 263, 270, 286, 299, 303, 305, 308, 316, 319, 325,
                  344, 349, 350, 353, 363, 365, 371, 395, 414, 437, 453, 459, 463, 489, 500, 503, 512, 514, 515, 516,
                  518, 530, 553, 558, 573, 574, 578, 586, 590, 602, 607, 618, 636, 638, 647, 676, 690, 691, 716, 761,
                  767, 798, 811, 815, 836, 843, 849, 867, 882, 903, 919, 921, 943, 948, 958, 959, 980, 997]

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
        self.assertEqual(lca3, root.left.right.left.left,
                         f'Incorrect LCA {lca3}. Should be {root.left.right.left.left}')

    def test_invalid_leaves_bt(self):
        """Test for if requested nodes are not part of tree. Should return None"""

        root = Node(67)
        root.left = Node(11)
        root.right = Node(82)
        root.left.left = Node(4)
        root.left.right = Node(60)
        root.left.right.left = Node(52)

        stray_node1 = Node(33)
        stray_node2 = Node(76)

        lca = LCA.findLCA(root, stray_node1, stray_node2)

        self.assertEqual(lca, None, f'Incorrect LCA {lca}. Should be {None}')

    def test_empty_dag(self):
        """Tests an empty DAG. Considering an empyt DAG to not be a DAG"""

        graph = []
        lca = LCA.findLCA(graph)

        self.assertEqual(lca, False, f'Incorrect LCA {lca}. Should be {False}')

    def test_single_node_dag(self):
        """Tests a single node DAG"""

        graph = [0]
        lca = LCA.findLCA(graph, 0, 0)

        self.assertEqual(lca, 0, f'Incorrect LCA {lca}. Should be {0}')

    def test_simple_dag(self):
        """Tests a basic DAG"""

        graph = [[0, 1], [0, 2], [1, 3], [2, 3], [1, 4]]
        lca1 = LCA.findLCA(graph, 1, 2)
        lca2 = LCA.findLCA(graph, 1, 3)
        lca3 = LCA.findLCA(graph, 3, 4)

        self.assertEqual(lca1, 0, f'Incorrect LCA {lca1}. Should be {0}')
        self.assertEqual(lca2, 1, f'Incorrect LCA {lca2}. Should be {1}')
        self.assertEqual(lca3, 1, f'Incorrect LCA {lca3}. Should be {1}')

    def test_slides_dag(self):
        """Tests DAG given in slides"""

        graph = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6]]
        lca1 = LCA.findLCA(graph, 3, 2)
        lca2 = LCA.findLCA(graph, 0, 6)
        lca3 = LCA.findLCA(graph, 3, 5)

        self.assertEqual(lca1, 0, f'Incorrect LCA {lca1}. Should be {0}')
        self.assertEqual(lca2, 0, f'Incorrect LCA {lca2}. Should be {0}')
        self.assertEqual(lca3, 3, f'Incorrect LCA {lca3}. Should be {3}')

    def test_complex_dag(self):
        """Tests a complex DAG found online"""

        graph = [[0, 2], [0, 12], [0, 14], [1, 11], [1, 16], [1, 13], [2, 6], [2, 13], [2, 16], [3, 4], [3, 7], [3, 8],
                 [3, 13], [3, 14], [3, 16], [4, 7], [4, 15], [4, 18], [5, 10], [5, 16], [6, 18], [7, 8], [8, 13],
                 [8, 16], [8, 17], [9, 17], [9, 18], [10, 11], [10, 13], [10, 17], [11, 16], [11, 17], [12, 18],
                 [12, 19], [13, 14], [13, 15], [13, 18], [14, 19], [17, 18]]

        lca1 = LCA.findLCA(graph, 0, 19)
        lca2 = LCA.findLCA(graph, 17, 15)

        self.assertEqual(lca1, 0, f'Incorrect LCA {lca1}. Should be {0}')
        self.assertEqual(lca2, 4, f'Incorrect LCA {lca2}. Should be {4}')

    def test_slides_dag_multnodes(self):
        """Tests slides DAG LCA for multiple nodes"""

        graph = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6]]

        lca = LCA.findLCA(graph, 3, 6, 2)

        self.assertEqual(lca, 0, f'Incorrect LCA {lca}. Should be {0}')

    def test_complex_dag_multnodes(self):
        """Tests complex DAG LCA for multiple nodes"""

        graph = [[0, 2], [0, 12], [0, 14], [1, 11], [1, 16], [1, 13], [2, 6], [2, 13], [2, 16], [3, 4], [3, 7], [3, 8],
                 [3, 13], [3, 14], [3, 16], [4, 7], [4, 15], [4, 18], [5, 10], [5, 16], [6, 18], [7, 8], [8, 13],
                 [8, 16], [8, 17], [9, 17], [9, 18], [10, 11], [10, 13], [10, 17], [11, 16], [11, 17], [12, 18],
                 [12, 19], [13, 14], [13, 15], [13, 18], [14, 19], [17, 18]]

        lca1 = LCA.findLCA(graph, 5, 10, 19)
        lca2 = LCA.findLCA(graph, 1, 14, 18)

        self.assertEqual(lca1, 5, f'Incorrect LCA {lca1}. Should be {5}')
        self.assertEqual(lca2, 0, f'Incorrect LCA {lca2}. Should be {0}')

    def test_non_acyclic_graph(self):
        """Tests a simple, non-acyclic graph. Returns false because not DAG"""
        graph = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 2], [4, 0]]

        lca = LCA.findLCA(graph, 3, 2)
        self.assertEqual(lca, False, f'Incorrect LCA {lca}. Should be {False}')

    def test_invalid_nodes_dag(self):
        """Test for if requested nodes are not part of DAG. Should return False"""

        graph = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6]]

        lca = LCA.findLCA(graph, 7, 8)
        self.assertEqual(lca, None, f'Incorrect LCA {lca}. Should be {False}')

if __name__ == '__main__':
    unittest.main()
