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
        node=Node(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node
    
    def print(self):
        if self.head==None:
            raise Exception("list is empty")
        itr=self.head
        emp=""
        while itr:
            emp+=str(itr.data)+"-->"
            itr=itr.next
        print(emp)
    
    def insertat(self,pos,data):
        if pos <0 or pos>self.getlen():
            raise Exception("invalid range")
        if self.head==None:
            self.head=Node(data)
        count=0
        itr=self.head
        while itr:
            if count==pos-1:
                node=Node(data)
                node.next=itr.next
                itr.next=node
            count+=1
            itr=itr.next
    def remove(self,pos):
        if pos==0:
            self.head=self.head.next
        itr=self.head
        count=0
        while itr:
            if count==pos-1:
                itr.next=itr.next.next
            count+=1
            itr=itr.next
    def getlen(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    
    
if __name__=="__main__":
    ll=Linkedlist()
    ll.insertb(12)
    ll.insertb(54)
    ll.insertb(100)
    ll.print()
    
    ll.inserte(22)
    ll.inserte(21)
    ll.print()
    ll.insertat(3,11)
    ll.insertat(1,45)
    ll.print()

    ll.remove(3)
    ll.remove(0)
    ll.print()
    ll.getlen()
    