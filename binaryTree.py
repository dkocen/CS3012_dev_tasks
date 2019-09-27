class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = self.construct_bt(data)
        self.inorder = self.inorder(self.root)

    def create_node(self, data, i, created, root):
        if created[i] is not None:
            return

        created[i] = Node(i)

        if data[i] == -1:
            root[0] = created[i]
            return

        if created[data[i]] is None:
            self.create_node(data, data[i], created, root)

        p = created[data[i]]

        if p.left is None:
            p. left = created[i]
        else:
            p.right = created[i]

    def construct_bt(self, data):
        n = len(data)
        created = [None for i in range(n + 1)]

        root = [None]
        for i in range(n):
            self.create_node(data, i, created, root)

        return root[0]

    def inorder(self, root):
        if root is None:
            return []

        left_list = self.inorder(root.left)
        right_list = self.inorder(root.right)
        return left_list + [root.key] + right_list



if __name__ == '__main__':
    data = [-1, 0, 0, 1, 1, 3, 5]
    bt= BinaryTree(data)
    print(bt.inorder)


