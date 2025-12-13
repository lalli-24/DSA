class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def remove(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head
        temp = self.head
        prev = None
        while temp:
            if prev is not None and temp.data == prev.data:
                temp = temp.next
                prev.next = temp
            else:
                prev = temp
                temp = temp.next
        return
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
l = linkedlist()
l.insert(1)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(3)
l.remove()
l.display()
