#  Invert the Binary Tree: Given a binary tree A, invert the binary tree and return it.
# Inverting refers to making the left child the right child and vice versa.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
		if A is None:
            return None
        left_tree = self.invertTree(A.left)
        right_tree = self.invertTree(A.right)
        A.left = right_tree
        A.right = left_tree
        return A

