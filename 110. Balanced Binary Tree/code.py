# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.ans = True
        
        def depth(r):
            if not r:
                return 0
            left = depth(r.left)
            right = depth(r.right)
            if abs(left-right)>1:
                self.ans=False
            return max(left,right)+1
        
        depth(root)
        return self.ans