# LeedCode June Challange Day 15
# Binary Search Tree Problem

# Given the root node of a binary search tree (BST) and a value. 
# You need to find the node in the BST that the node's value equals the given value. 
# Return the subtree rooted with that node. 
# If such node doesn't exist, you should return NULL.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3

# And the value to search: 2
# You should return this subtree:
#       2     
#      / \   
#     1   3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    while(root != None):
        if(val == root.val):
            return root
        if(val < root.val):
            return self.searchBST(root.left, val)
        elif(val > root.val):
            return self.searchBST(root.right, val)
    return None