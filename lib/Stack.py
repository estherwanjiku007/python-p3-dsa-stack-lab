class Stack:

    def __init__(self, items = [], limit = 100): 
        self.items=items       
        self.dictionary={}
        for value in items:
            self.dictionary[value]=True
        self.limit=limit

    def isEmpty(self):  
        for value in self.dictionary:
            return False if value else True 
                # if len(self.items)!=0:
        #    return True
        # else:return False

    def push(self, item):
        self.dictionary[item]=True
        return self

    def pop(self):
        self.dictionary.pop(self)
        return self

    def peek(self):
        return self.dictionary[self]
        
    
    def size(self):
        return len(self.dictionary)

    def full(self):
        for value in self.dictionary:
            return True if value else False
    def search(self, target):
        pass
