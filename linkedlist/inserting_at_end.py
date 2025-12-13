class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
    def display(self):
        temp = self.head
        while temp:
           print(temp.data, end='->')
           temp = temp.next
        print('Null')
ll = linkedlist()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.display()
