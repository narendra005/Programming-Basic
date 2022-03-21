# Symmetric Binary Tree: Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class Solution:
    # @param A : root node of tree
    # @return an integer
    def check(self, node1, node2):
        if node1 == None and node2 == None:
            return 1
        if (node1 == None and node2 != None) or (node1 != None and node2 == None):
            return 0
        if node1.val != node2.val:
            return 0
        if self.check(node1.left, node2.right) and self.check(node1.right, node2.left):
            return 1
        else:
            return 0

    def isSymmetric(self, A):
        return self.check(A, A)