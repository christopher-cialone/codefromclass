from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
            

        # we need at least one base case
        # we need what to do in every other situation


        # what are we doing at each node?
        # pre-step (other base case): is there a node? Is there an edge case Im not thinking about
            # if not: return None
        # is node.val == val?
            # if so return that node
        # is node.val > val:
            # if so check to the left of that node
        # is node.val < val:
            # if so check to the right of that node




# In computer science, a "tree" is a hierarchical data structure that consists of nodes connected by
# edges. Each node in a tree can have zero or more child nodes, except for the root node, which has no
# parent. A tree is a type of directed acyclic graph, meaning that it is a graph with directed edges 
# and no cycles.

# Trees are commonly used in data structures and algorithms to represent hierarchical relationships, such as in
#  file systems, HTML documents, organizational charts, and decision trees. Some common types of trees include 
#  binary trees, n-ary trees, and balanced trees like AVL trees and red-black trees.

# A binary tree is a type of tree in which each node has at most two child nodes, referred to as the left child
#  and the right child. Here's an example of a binary tree:


# Copy code
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# In this binary tree, the root node has two child nodes, which in turn have two child nodes each.
#  The leaf nodes are the nodes with no child nodes (4, 5, 6, and 7 in this example).

# Trees can be traversed in different ways, depending on the order in which you visit the nodes. Some 
# common tree traversal algorithms include depth-first search (DFS) and breadth-first search (BFS). In 
# DFS, you visit as deep as possible along each branch before backtracking, while in BFS, you visit all
#  the nodes at the same depth before moving on to the next depth level. These traversal algorithms are 
#  used in many tree-based algorithms, such as searching, sorting, and optimization problems.



