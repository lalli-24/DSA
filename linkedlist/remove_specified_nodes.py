class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head == None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def remove(self,val):
        if self.head==None:
            return None
        while self.head and self.head.data==val:
            self.head=self.head.next
        temp=self.head
        prev=None
        while temp:
            if temp.data!=val:
                prev=temp
                temp=temp.next
            else:
                temp=temp.next
                prev.next=temp
        return
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
l=linkedlist()
l.insert(1)
l.insert(2)
l.insert(6)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.remove(6)
l.display()
