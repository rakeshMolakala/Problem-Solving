class LinkedNode:
    def __init__(self,key=0,val=0,prev=None,nex=None):
        self.val=val
        self.key=key
        self.freq = 1
        self.prev=prev
        self.next=nex

class DLL:
    def __init__(self):
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert(self,node):
        # insert just after head node
        temp = self.head.next 
        temp.prev = node
        node.next = temp
        self.head.next = node
        node.prev = self.head
        self.size +=1
        
    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -=1

        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        # frequency to doubly LL
        self.map1 = dict()
        # key to LL node
        self.map2 = dict()
        self.leastFreq = 0

    def get(self, key: int) -> int:
        if(key in self.map2):
            temp = self.map2[key]
            self.updateFreq(temp)
            return temp.val
        return -1

    def put(self, key: int, val: int) -> None:
        if(self.cap==0):
            return 
        if(key in self.map2):
            temp = self.map2[key]
            temp.val = val
            self.updateFreq(temp)
        else:
            if(self.size==self.cap):
                leastFreqLL = self.map1[self.leastFreq]
                removeNode = leastFreqLL.tail.prev
                self.map2.pop(removeNode.key)
                leastFreqLL.remove(removeNode)
                self.size-=1
                
            self.leastFreq = 1
            node = LinkedNode(key,val)
            self.map2[key] = node
            self.size+=1
            if(1 in self.map1):
                self.map1[1].insert(node)
            else:
                newDll = DLL()
                newDll.insert(node)
                self.map1[1] = newDll
        
    def updateFreq(self,node):
        currFreq = node.freq
        currLL = self.map1[currFreq]
        currLL.remove(node)
        if(currFreq==self.leastFreq and currLL.size==0):
            self.leastFreq+=1
        newFreq = currFreq+1
        node.freq = newFreq
        if(newFreq in self.map1):
            self.map1[newFreq].insert(node)
        else:
            newDll = DLL()
            newDll.insert(node)
            self.map1[newFreq] = newDll
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)