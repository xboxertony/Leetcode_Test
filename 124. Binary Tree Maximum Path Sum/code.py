class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float("-inf")
        def max_gain_from_node(node):
            nonlocal maxSum
            if not node:
                return 0

            leftGain = max(max_gain_from_node(node.left), 0)
            rightGain = max(max_gain_from_node(node.right), 0)
            
            priceNewpath = node.val + leftGain + rightGain            

            maxSum = max(maxSum, priceNewpath)

            return node.val + max(leftGain, rightGain)
   
        max_gain_from_node(root)
        return maxSum