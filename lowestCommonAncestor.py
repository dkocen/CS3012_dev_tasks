from binarytree import Node
import networkx as nx


def findLCA(graph=None, *args):
    if isinstance(graph, Node):
        return findLCABinaryTree(graph, args[0], args[1])
    elif isinstance(graph, list):
        return findLCAdag(graph, args)
    else:
        return False

def findLCABinaryTree(root, n1, n2):
    # Base Case
    if n1 == n2:
        return n1
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root == n1 or root == n2:
        return root

        # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

        # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

def findLCAdag(graph, args):

    # Convert to networkX diGraph
    g = nx.DiGraph(graph)
    if nx.is_directed_acyclic_graph(g):
        return nx.lowest_common_ancestor(g, args[0], args[1])