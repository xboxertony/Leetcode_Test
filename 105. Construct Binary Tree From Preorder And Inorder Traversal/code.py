class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        v = preorder[0]
        preorder.remove(v)
        root = TreeNode(v)
        head = inorder.index(v)
        root.left = self.buildTree(preorder,inorder[:head])
        root.right = self.buildTree(preorder,inorder[head+1:])
        return root