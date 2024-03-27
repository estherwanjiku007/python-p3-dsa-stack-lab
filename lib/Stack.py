class Stack:
    def __init__(self, items=[], limit=100):
           
        self.items = items
        self.limit = limit

    def isEmpty(self):
      if not self.items:
          return True
      else:return False

    def push(self, item):
       
        if self.full():
            return False
        else:
            self.items.append(item)
        return self.items

    def pop(self):
        if self.items:
           self.items.pop()
        else:return False
    def peek(self):
        if not self.isEmpty():
            
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):        
        if self.limit and len(self.items)==self.limit:
            return True
        else:return False

    def search(self, target):
        
        if target in self.items:
            
            value=len(self.items)-self.items.index(target)-1
            return value
        else:return -1
