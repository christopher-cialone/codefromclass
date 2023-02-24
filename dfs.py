# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root) -> list[int]:
        
        self.result = []

        return self.result

    def traverse(self, node):
        # need out base case: if we see a node that is null, return
        # assuming we are looking at a real node:
        # pre-prder traversal: going all the way down and recording what we see on the way
        # add the value we see to our results list
        # recurse to the left (by calling traverse() agian)
        # recurse to the right (by calling traverse() agian)

        if node == None:
            return
        self.result.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)
        