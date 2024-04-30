class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtStart(self,data):
        if self.head==None:
            self.head=Node(data,self.head)
        else:
            node=Node(data,self.head)
            self.head.prev=node
            self.head=node
    def insertAtEnd(self,data):
        if self.head==None:
            self.insertAtStart(data)
            return
        ctr=self.head
        while ctr.next:
            ctr=ctr.next
        node=Node(data,None,ctr)
        ctr.next=node
    def delete(self,pos):
        if pos==0:
            self.head=self.head.next
        if pos<0 or pos>self.getlen():
            raise Exception("invalid range")
        ctr=self.head
        count=0
        while ctr:
            if count==pos-1:
                node=ctr.next.next
                node.prev=node.prev.prev
                ctr.next=ctr.next.next
            count+=1
            ctr=ctr.next
    def insertatval(self,pos,data):
        ctr=self.head
        count=0
        if pos==0:
            self.insertAtStart(data)
        if pos<0 or pos>self.getlen():
            raise Exception("invalid range given")
        while ctr:
            if count==pos-1:
                node=Node(data,ctr.next,ctr)
                ctr.next.prev=node
                ctr.next=node
            count+=1
            ctr=ctr.next
        
    def search(self,data):
        ctr=self.head
        count=0
        while ctr:
            if ctr.data==data:
                print(f"the value {data} found at pos {count}")
            ctr=ctr.next
            count+=1
    def getlen(self):
        count=0
        ctr=self.head
        while ctr:
            count+=1
            ctr=ctr.next
        return count        
    def printdll(self):
        ctr=self.head
        emp=""
        while ctr:
            emp+=str(ctr.data)+"-->"
            ctr=ctr.next
        print(emp)
    def revprint(self):
        ctr=self.head
        emp=""
        while ctr.next:
            ctr=ctr.next
        while ctr:
            emp+=str(ctr.data)+"-->"
            ctr=ctr.prev
        print(emp)
if __name__=='__main__':    
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(34)
    dll.insertAtEnd(87)
    dll.insertAtStart(45)
    dll.printdll()
    dll.revprint()
    #dll.delete(3)
    #dll.delete(1)
    dll.delete(2)
    
    dll.insertatval(1,40)
    dll.insertatval(1,15)
    dll.insertatval(0,100)
    """
    dll.insertatval(0,12)
    dll.insertAtEnd(5)
    dll.search(100)
    dll.search(350)
   """
    dll.search(100)
    dll.printdll()
    dll.revprint()