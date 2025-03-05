class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,max_val):
            nonlocal ans
            if not node:
                return
            if node.val>=max_val:
                ans+=1
            dfs(node.left,max(max_val,node.val))
            dfs(node.right,max(max_val,node.val))
        dfs(root,-float("inf"))
        return ans