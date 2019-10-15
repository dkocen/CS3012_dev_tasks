# CSU3012_dev_task

Development tasks repo for TCD CSU3012 Software Engineering

## Dev Task 1 and 2: LCA for Binary Tree and Directed Acyclic Graph

The first task is to find an algorithm online for retrieving the LCA of a binary tree and to properly unit test it.

The second task adds functionality for finding the LCA of any directed acyclic graph.

### Dependencies
- [BinaryTree](https://pypi.org/project/binarytree/) (for building binary trees)
- [Networkx](https://networkx.github.io/) (for building and analyzing DAGs)
- [Unittest](https://docs.python.org/2/library/unittest.html) (for unit testing)

### Function Inputs
- Graph: The variable referencing the graph being explored. 
	- If binary tree this should be the root Node instance (see [BinaryTree](https://pypi.org/project/binarytree/) for instantiation of Node class).
	- If DAG should be list of lists containing nodes and edges. For instance [[0,1], [0,2], [1, 2]] would be a DAG with nodes 0, 1, 2 and edges pointing 0->1, 0->2, and 1->2.
	- If graph takes any other form the function will return False.
- *args: The various nodes to find the LCA of.
	- If binary tree should be Node instances
	- If DAG should be node numbers

### Function Outputs
Returns Node instance if finding the LCA of a binary tree.

Returns node number if finding the LCA of a DAG.

Returns None if no LCA exists (usually asking to find LCA of node that is not part of tree or DAG).

Returns False if graph is neither a Node instance or list of list corresponding to a DAG.

### Current Issues
- Does not work if requesting to find LCA of more than two nodes.
- Does not work for trees that are non-binary.
- Only works with integer values in Nodes for binary tree. Can have repeats though.
- Only works for integer values for nodes in DAG. Cannot have repeat values either.
