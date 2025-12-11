class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def reverse(self):
        if self.head == None:
            return
          
        temp=self.head
        prev=None
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        self.head=prev
        return
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print('None')
l=linkedlist()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.reverse()
l.display()
