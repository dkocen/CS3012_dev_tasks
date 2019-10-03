from binarytree import tree, bst, heap, build
import networkx as nx

my_tree1 = tree(height=0)
my_tree1list = list(my_tree1)

print(my_tree1list)

print(my_tree1)
my_tree2 = tree(height=1, is_perfect=True)
print(my_tree2.value)
my_tree3 = tree(height=3, is_perfect=False)
my_heap = heap(height=3)
print(my_tree1)
print(my_tree2)
print(my_tree3)
print(my_heap)

root = None
print(root.inorder)

values = [10, 12, 14, 24, 39, 50, 54, 62, 67, 92, 134, 153, 161, 162, 167, 171, 172, 173, 191, 193, 197, 205, 206, 208, 210, 211, 222, 239, 240, 246, 249, 253, 263, 270, 286, 299, 303, 305, 308, 316, 319, 325, 344, 349, 350, 353, 363, 365, 371, 395, 414, 437, 453, 459, 463, 489, 500, 503, 512, 514, 515, 516, 518, 530, 553, 558, 573, 574, 578, 586, 590, 602, 607, 618, 636, 638, 647, 676, 690, 691, 716, 761, 767, 798, 811, 815, 836, 843, 849, 867, 882, 903, 919, 921, 943, 948, 958, 959, 980, 997]
root = build(values)
print(root)


