class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insertb(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head==None:
            print("empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
        
ll=Linkedlist()
ll.insertb(12)
ll.insertb(24)
ll.insertb(48)
ll.print()