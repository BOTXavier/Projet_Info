class Stack(object): 
    "pile"
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        " recuperer l'element le plus haut"
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0


