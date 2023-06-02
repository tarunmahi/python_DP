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
        if self.head==None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def print(self):
        if self.head==None:
            print("linked list empty")
            return
        itr=self.head
        empstr=""
        while itr:
            empstr+=str(itr.data)+"-->"
            itr=itr.next
            
        print(empstr)
    
    def getl(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove(self,index):
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
        
        
ll=Linkedlist()
ll.insertb(12)
ll.insertb(35)
ll.inserte(1)
ll.insertb(2)
ll.print()
ll.remove(2)
ll.print()