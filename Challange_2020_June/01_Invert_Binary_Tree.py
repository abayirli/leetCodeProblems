# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(root):
            if(root.right != None or root.left != None):
                temp = root.right
                root.right = root.left
                root.left = temp
            self.invertTree(root.right)
            self.invertTree(root.left) 
        return root