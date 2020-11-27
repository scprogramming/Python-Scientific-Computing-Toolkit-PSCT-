class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = next

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def setNext(self,next):
        self.next = next

    def setValue(self,value):
        self.value = value