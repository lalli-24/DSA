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
    def count(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp=self.head
        mid=count//2
        for x in range(mid):
            temp=temp.next
        self.head=temp
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
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.count()
l.display()
