class LinkedNode:
    def __init__(self,key=0,val=0,prev=None,nex=None):
        self.val=val
        self.key=key
        self.prev=prev
        self.next=nex

class DoublyLL:
    def __init__(self):
        self.head = LinkedNode(0,0)
        self.tail = LinkedNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def moveNodeToFront(self,node):
        # if(self.size==0):
        #     return
        prevNode = node.prev
        nextNode = node.next
        nextNode.prev = prevNode
        prevNode.next = nextNode
        
        #now we need to add it to front
        self.addNodeAtFront(node)
        
        
    def addNodeAtFront(self,node):
        temp1 = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp1
        temp1.prev = node
        self.size+=1
        
    def deleteLastNode(self):
        # if(self.size==0):
        #     return
        temp = self.tail.prev
        temp2 = temp.prev
        temp2.next = self.tail
        self.tail.prev = temp2
        self.size-=1
        
    def getLastNodeKey(self):
        return self.tail.prev.key
        
class LRUCache:
    def __init__(self, capacity: int):
        self.dl = DoublyLL()
        self.dic = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if(key not in self.dic):
            return -1
        temp1 = self.dic[key]
        self.dl.moveNodeToFront(temp1)
        return temp1.val
        
                
    def put(self, key: int, value: int) -> None:
        if(key in self.dic):
            node = self.dic[key]
            node.val = value
            self.dl.moveNodeToFront(node)
        else:
            newNode = LinkedNode(key,value)
            self.dic[key] = newNode
            if(self.cap>0):
                self.dl.addNodeAtFront(newNode)
                self.cap-=1
            else:
                lastNodeKey = self.dl.getLastNodeKey()
                self.dic.pop(lastNodeKey)
                self.dl.deleteLastNode()
                self.dl.addNodeAtFront(newNode)
            
                
        








# class LinkedNode:
#     def __init__(self,key=0,val=0,prev=None,nex=None):
#         self.val=val
#         self.key=key
#         self.prev=prev
#         self.next=nex

# class DoublyLL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size=0
    
#     def addNodeAtEnd(self,key,val,prev=None,nex=None):
#         if(self.head):
#             self.head.next=LinkedNode(key,val,self.head)
#             self.head=self.head.next
#         else:
#             self.head = LinkedNode(key,val)
#             self.tail=self.head
            
#     def getHead(self):
#         return self.head
    
#     def getTail(self):
#         return self.tail
    
#     def rearrangeDll(self,temp1):
#         if(temp1.prev==None):
#             self.tail=temp1.next
#             self.tail.prev=None
#         else:
#             temp1.prev.next=temp1.next
#             if(temp1.next):
#                 temp1.next.prev=temp1.prev
                
#         temp1.next=None
#         temp3=self.getHead()
#         temp3.next=temp1
#         temp1.prev=temp3
#         self.head=temp1
        
    
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.dl = DoublyLL()
#         self.dic = dict()
#         self.cap = capacity

#     def get(self, key: int) -> int:
#         if(key not in self.dic):
#             return -1
#         temp1 = self.dic[key]
#         if(temp1.next==None and temp1.prev==None):
#             return self.dic[key].val
#         if(temp1.next==None):
#             return self.dic[key].val
#         self.dl.rearrangeDll(temp1)
#         return self.dic[key].val
                
#     def put(self, key: int, value: int) -> None:
#         if(self.cap>0 and (key not in self.dic)):
#             self.dl.addNodeAtEnd(key,value)
#             self.dic[key]=self.dl.getHead()
#             self.cap-=1
#         elif(key in self.dic):
#             temp1 = self.dic[key]
#             if(not temp1.val==value):
#                 temp1.val=value
#             if(temp1.next==None and temp1.prev==None):
#                 return 
#             if(temp1.next==None):
#                 return 
#             self.dl.rearrangeDll(temp1)

#         elif(self.cap==0 and (key not in self.dic)):
#             temp = self.dl.getTail()
#             if(temp.next):
#                 self.dl.tail=temp.next
#                 self.dl.tail.prev=None
#             else:
#                 self.dl.tail=None
#                 self.dl.head=None
#             temp.next=None
#             self.dic.pop(temp.key)
#             self.dl.addNodeAtEnd(key,value)
#             self.dic[key]=self.dl.getHead()
                        
            
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)