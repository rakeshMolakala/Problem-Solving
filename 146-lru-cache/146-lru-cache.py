# class LinkedNode:
#     def __init__(self,key=0,val=0,prev=None,nex=None):
#         self.val=val
#         self.key=key
#         self.prev=prev
#         self.next=nex

# class DoublyLL:
#     def __init__(self):
#         self.head = LinkedNode(0,0)
#         self.tail = LinkedNode(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
    
#     def moveNodeToFront(self,node):
#         prevNode = node.prev
#         nextNode = node.next
#         nextNode.prev = prevNode
#         prevNode.next = nextNode
        
#         #now we need to add it to front
#         self.addNodeAtFront(node)
        
        
#     def addNodeAtFront(self,node):
#         temp1 = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = temp1
#         temp1.prev = node
        
#     def deleteLastNode(self):
#         temp = self.tail.prev
#         temp2 = temp.prev
#         temp2.next = self.tail
#         self.tail.prev = temp2
        
#     def getLastNodeKey(self):
#         return self.tail.prev.key
        
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.dl = DoublyLL()
#         self.dic = dict()
#         self.cap = capacity

#     def get(self, key: int) -> int:
#         if(key not in self.dic):
#             return -1
#         temp1 = self.dic[key]
#         self.dl.moveNodeToFront(temp1)
#         return temp1.val
        
                
#     def put(self, key: int, value: int) -> None:
#         if(key in self.dic):
#             node = self.dic[key]
#             node.val = value
#             self.dl.moveNodeToFront(node)
#         else:
#             newNode = LinkedNode(key,value)
#             self.dic[key] = newNode
#             if(self.cap>0):
#                 self.dl.addNodeAtFront(newNode)
#                 self.cap-=1
#             else:
#                 lastNodeKey = self.dl.getLastNodeKey()
#                 self.dic.pop(lastNodeKey)
#                 self.dl.deleteLastNode()
#                 self.dl.addNodeAtFront(newNode)



class LinkedNode:
    def __init__(self,key=0,val=0,prev=None,nex=None):
        self.val=val
        self.key=key
        self.prev=prev
        self.next=nex

class LRUCache:
    def __init__(self, capacity: int):
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if(key not in self.dic):
            return -1
        temp = self.dic[key]
        self.remove(temp)
        self.insert(temp)
        return temp.val
        
                
    def put(self, key: int, value: int) -> None:
        if(key in self.dic):
            temp = self.dic[key]
            self.remove(temp)
            newNode = LinkedNode(key,value)
            self.insert(newNode)
        else:
            newNode = LinkedNode(key,value)
            if(self.cap>0):
                self.insert(newNode)
                self.cap-=1
            else:
                self.remove(self.tail.prev)
                self.insert(newNode)
                
    def insert(self,node):
        # insert just after head node
        self.dic[node.key] = node
        temp = self.head.next 
        temp.prev = node
        node.next = temp
        self.head.next = node
        node.prev = self.head
        
    def remove(self,node):
        # removing the last node to right, which is attached left to tail
        self.dic.pop(node.key)
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)