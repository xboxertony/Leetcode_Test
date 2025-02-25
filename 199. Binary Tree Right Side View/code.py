class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        r = root
        arr = [r] if r else []
        ans = [r.val] if r else []
        while arr:
            temp = []
            for node in arr:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                ans.append(temp[-1].val)
            arr = temp[:]
        return ans