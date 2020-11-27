from DataStructures.Node import Node
class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        inVal = Node(value,None)

        if self.top is None:
            self.top = inVal
        else:
            inVal.setNext(self.top)
            self.top = inVal

        self.size += 1

    def peek(self):
        return self.top.getValue()

    def pop(self):
        if self.top is not None:
            value = self.top.getValue()
            self.top = self.top.getNext()
            self.size -= 1
            return value

    def isEmpty(self):
        return self.size == 0