class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def coun(self):
        c = 0
        temp = self.head
        while temp:
            temp = temp.next
            c += 1
        return c
ll=linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print(ll.coun())
