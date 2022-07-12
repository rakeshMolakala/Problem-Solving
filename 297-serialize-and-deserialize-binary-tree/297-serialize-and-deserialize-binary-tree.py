# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        global res
        res = ""
        
        def preorder(root):
            if not root:
                global res
                res = res + ',' + 'n' 
                return
            res = res + ',' + str(root.val) 
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return res[1:]

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        
        def dfs():
            if(vals[self.i]=='n'):
                self.i+=1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))