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
    def insert_at_k(self,data,k):
        new=Node(data)
        if k==0:
            new.next=self.head
            self.head=new
            return
        temp=self.head
        c=0
        while temp is not None and c<k-1:
            temp=temp.next
            c+=1
        if temp is None:
            print("Invalid position")
            return
        new.next=temp.next
        temp.next=new
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print('Null')
ll=linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert_at_k(30,1)
ll.display()
