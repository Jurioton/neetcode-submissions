class MinStack:

    def __init__(self):
        self.items =[]
        

    def push(self, val: int) -> None:
        self.items.append(val)
        return None
        

    def pop(self) -> None:
        self.items.pop()
        return None
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return min(self.items)
        
