# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N;"
        s = ""
        s+=str(root.val)+";"
        s+=self.serialize(root.left)
        s+=self.serialize(root.right)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        arr = data.split(";")[:-1]
        print(arr)
        def find_root(array):
            node_val = array.pop(0)
            if node_val=="N":
                return None
            root = TreeNode(node_val)
            root.left = find_root(array)
            root.right = find_root(array)
            return root
        return find_root(arr)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))