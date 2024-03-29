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
    left_lca = findLCABinaryTree(root.left, n1, n2)
    right_lca = findLCABinaryTree(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

        # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


def findLCAdag(graph, args):
    # Check if empty graph
    if not graph:
        return False

    # If graph is just a single node reformat graph so it is a node with a self-loop
    # This allows the nx.DiGraph function to work
    if len(graph) == 1:
        value = graph[0]
        graph = [[value, value]]
    # Convert to networkX diGraph
    g = nx.DiGraph(graph)

    # Check to make sure node is actually in graph
    for arg in args:
        if not g.has_node(arg):
            return None

    if nx.is_directed_acyclic_graph(g):
        return nx.lowest_common_ancestor(g, args[0], args[1])
    else:
        return False
