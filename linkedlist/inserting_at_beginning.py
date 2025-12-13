class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def display(self):
        temp = self.head
        while temp:
           print(temp.data, end='->')
           temp = temp.next
        print('Null')

ll = linkedlist()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.display()
