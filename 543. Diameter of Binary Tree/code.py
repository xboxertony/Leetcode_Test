# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def depth(r):
            if not r:
                return 0
            left = depth(r.left)
            right = depth(r.right)
            self.best = max(self.best,left+right)
            return max(left,right)+1
        depth(root)
        return self.best