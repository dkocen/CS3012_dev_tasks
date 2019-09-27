class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def create_node(data, i, created, root):
    if created[i] is not None:
        return

    created[i] = Node(i)

    if data[i] == -1:
        root[0] = created[i]
        return

    if created[data[i]] is None:
        create_node(data, data[i], created, root)

    p = created[data[i]]

    if p.left is None:
        p. left = created[i]
    else:
        p.right = created[i]


def construct_bt(data):
    n = len(data)
    created = [None for i in range(n + 1)]

    root = [None]
    for i in range(n):
        create_node(data, i, created, root)

    return root[0]

def inorder(root):
    if root is None:
        return []

    left_list = inorder(root.left)
    right_list = inorder(root.right)
    return left_list + [root.key] + right_list



if __name__ == '__main__':
    data = [-1, 0, 0, 1, 1, 3, 5]
    root = construct_bt(data)
    print('Inorder traversal of constructed tree:')
    print(inorder(root))



