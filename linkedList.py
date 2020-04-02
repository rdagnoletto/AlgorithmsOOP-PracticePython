class LinkedList:
    def __init__(self):
            self.head = None
            self.tail = None
    class Node:
        def __init__(self,val,next=None):
            self.val = val
            self.next = next

    def addToFront(self, val):
        node = self.Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addToEnd(self, val):
        node = self.Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def printList(self):
        n = self.head
        listString = "head->"
        while(n is not None):
            listString += "%d->" %n.val
            n = n.next

        print(listString+"->tail")
            

l = LinkedList()
l.addToEnd(5)
l.addToEnd(2)
l.addToFront(7)
l.addToFront(3)
l.addToEnd(4)
l.addToEnd(1)
l.addToFront(6)
l.addToFront(9)

l.printList()