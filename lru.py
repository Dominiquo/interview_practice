
class doubleLink(object):
    def __init__(self,key,val,pre,aft):
        self.key = key
        self.val = val
        self.pre = pre
        self.aft = aft
    def getPre(self):
        return self.pre
    def getPost(self):
        return self.post
    def getVal(self):
        return self.val
    def getKey(self):
        return self.key
    
class LRU(object):
    def __init__(self,capacity):
        self.cap = capacity
        self.size = 0
        self.lru = None
        self.mru = None
        self.hash = {}
    
    def get(self,key):
        if key not in self.hash:
            return "key is not in cache"
        else:
            node = self.hash[key]
            if node == self.lru:
                node.aft.pre = None
                self.lru = node.aft
                node.pre = self.mru
                self.mru = node
                node.aft = None
            elif node != self.mru:
                node.pre.aft = node.aft
                node.aft.pre = node.pre
                node.pre = self.mru
                self.mru = node
                node.aft = None
        return node.getVal()
                
        
    def put(self,key,val):
        if (self.size+1) > self.cap:
            self.lru = self.lru.aft
            self.lru.pre = None
            newNode = doubleLink(key,val,self.mru,None)
            self.mru.aft = newNode
            self.mru = newNode
            self.hash[key] = newNode
        elif self.size > 0:
            self.size += 1
            newNode = doubleLink(key,val,self.mru,None)
            self.mru.aft = newNode
            self.mru = newNode
            self.hash[key] = newNode
        else:
            newNode = doubleLink(key,val,None,None)
            self.mru = newNode
            self.lru = newNode
            self.size += 1
        return True
    
f,i = "First",1
s,e = "Second",2
t,h = "Third",3
mylru = LRU(2)
mylru.put(f,i)
mylru.put(s,e)
mylru.put(t,h)

#currently has 2 and 3 in there

mylru.get(f) #shouldn't be in there since it got bumped out
mylru.get(s)
