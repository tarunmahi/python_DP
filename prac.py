class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None
    def insertb(self,data):
        if not self.head:
            node=Node(data,self.head)
            self.head=node
        node=Node(data,self.head)
        self.head=node
    def inserte(self,data):
        if self.head==None:
            self.insertb(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)
    def print(self):
        if self.head==None:
            print("list is empty")
        itr=self.head
        emp=""
        while itr:
            emp=emp+str(itr.data)+"->"
            itr=itr.next
        print(emp)


if __name__=="__main__":
    ll=Linkedlist()
    ll.insertb(34)
    ll.insertb(12)
    ll.inserte(22)
    ll.inserte(21)
    ll.print()
    """
    ll.insertat(3,11)
    ll.insertat(1,45)
    ll.print()
    ll.remove(3)
    ll.print()
    ll.getlength()"""