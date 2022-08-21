# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if not root:
            return ""
        res = ""
        q = deque()
        q.append(root)
        while(q):
            curr = q.popleft()
            if(curr==None):
                res = res + 'None' + ','
            else:
                res = res + str(curr.val)+','
                q.append(curr.left)
                q.append(curr.right)
        res = res[0:-1]
        return res
            
    def deserialize(self, data):
        if(data==""):
            return None
        lis = data.split(',')
        n = len(lis)
        q = collections.deque()
        root = TreeNode(lis[0])
        q.append(root)
        index = 0
        while(q):
            curr = q.popleft()
            if(lis[index+1]!='None'):
                curr.left = TreeNode(lis[index+1])
                q.append(curr.left)
            if(lis[index+2]!='None'):
                curr.right = TreeNode(lis[index+2])
                q.append(curr.right)
            index=index+2
        return root
            
            
            
        
        
        
        
        
        
        
#     def serialize(self, root):
#         global res
#         res = ""
        
#         def preorder(root):
#             if not root:
#                 global res
#                 res = res + ',' + 'n' 
#                 return
#             res = res + ',' + str(root.val) 
#             preorder(root.left)
#             preorder(root.right)
            
#         preorder(root)
#         return res[1:]

#     def deserialize(self, data):
#         vals = data.split(',')
#         self.i = 0
        
#         def dfs():
#             if(vals[self.i]=='n'):
#                 self.i+=1
#                 return None
#             root = TreeNode(int(vals[self.i]))
#             self.i+=1
#             root.left = dfs()
#             root.right = dfs()
#             return root
        
#         return dfs()
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))