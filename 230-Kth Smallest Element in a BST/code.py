class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0
        ans = None

        def find_tree(r):
            nonlocal cnt,ans
            if not r or cnt>k:
                return
            find_tree(r.left)
            cnt+=1
            if cnt==k:
                ans = r.val
                return
            find_tree(r.right)
        

        find_tree(root)
        return ans