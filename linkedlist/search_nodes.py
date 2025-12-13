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
    def search(self,k):
        temp=self.head
        while temp:
            if temp.data==k:
                return True
            temp=temp.next
        return False
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
l.display()
print(l.search(10))
print(l.search(12))
