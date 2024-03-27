class Stack:
    def __init__(self, items = [], limit = 100): 
        self.items=items       
        self.dictionary={}
        for value in items:
            self.dictionary[value]=True
        self.limit=limit

    def isEmpty(self): 
        return not bool(self.items) 
        # for value in self.items:
        #     #return False if value else True 
        #     if value:
        #         return False
        #     else:return True
        #         # if len(self.items)!=0:
        #    return True
        # else:return False

    def push(self, item):
        self.items.append(item)
        return self

    def pop(self):
        items=[]
        if not self.isEmpty():
            return self.pop()
        else:return None
    def peek(self):
        return self.dictionary[self]
        
    
    def size(self):
        return len(self.dictionary)

    def full(self):
        return bool(self.items)
    def search(self, target):
        diff=0
        diff+=(self.items.index(target)-0)
        return diff
