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
        
    def inserte(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    
    
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
ll.inserte(34)
ll.insertb(48)
ll.print()