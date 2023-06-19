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
            self.insertb(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
            
    def insertat(self,pos,data):
        if pos<0 or pos>self.getlength():
            raise Exception("invalid range given")
        if pos==0:
            self.insertb(data)
        itr=self.head
        count=0
        while itr:
            if count==pos-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1
        
    def remove(self,pos):
        if pos<0 or pos>self.getlength():
            raise Exception("invalid range")
        if pos==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==pos-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
    def getlength(self):
        count=0
        
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count
    def print(self):
        
        if self.head==None:
            print("empty list")
        itr=self.head
        emp_str=""
        while itr:
            emp_str+=str(itr.data)+"-->"
            itr=itr.next
        print(emp_str)


if __name__=="__main__":
    ll=Linkedlist()
    ll.insertb(34)
    ll.insertb(12)
    ll.inserte(22)
    ll.inserte(21)
    ll.print()
    ll.insertat(3,11)
    ll.insertat(1,45)
    ll.print()
    ll.remove(3)
    ll.print()
    ll.getlength()