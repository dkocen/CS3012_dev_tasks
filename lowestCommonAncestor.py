class LowestCommonAncestor:
    def __init__(self, root, p, q):
        self.answer = None
        self.lowest_common_ancestor(root, p, q)

    def lowest_common_ancestor(self, root, p, q):
        """
        :param root: TreeNode
        :param p: TreeNode
        :param q: TreeNode
        :return: TreeNode
        """

        def recurse_tree(current_node):
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            mid = current_node.value == p or current_node.value == q

            if mid + left + right >= 2:
                self.answer = current_node

            return mid or left or right

        recurse_tree(root)
