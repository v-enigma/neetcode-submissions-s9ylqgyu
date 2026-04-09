class MinStack:

    def __init__(self):
        self.storage = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.storage.insert(0,val)
        if  self.min is None:
            self.min = val
        elif self.min > val:
            self.min = val
        

    def pop(self) -> None:
        removed = self.storage.pop(0)
        if removed == self.min:
            if len(self.storage) == 0 :
                self.min = None
                return 
            self.min = self.storage[0]
            for i in range(1,len(self.storage)):
                if self.min > self.storage[i]:
                    self.min = self.storage[i]

    def top(self) -> int:
        return self.storage[0]
        

    def getMin(self) -> int:
        return self.min

        
