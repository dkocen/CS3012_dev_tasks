from binarytree import tree, bst, heap
import networkx as nx

my_tree1 = tree(height=0)
my_tree1list = list(my_tree1)

print(my_tree1list)

print(my_tree1)
my_tree2 = tree(height=3, is_perfect=True)
my_tree3 = tree(height=3, is_perfect=False)
my_heap = heap(height=3)
print(my_tree1)
print(my_tree2)
print(my_tree3)
print(my_heap)

root = None
print(root.inorder)


