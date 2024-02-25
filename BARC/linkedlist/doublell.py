class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtStart(self,data):
        if self.head==None:
            node=Node(data,None,self.head)
            self.head=node
        else:
            node=Node(data,None,self.head)
            self.head.prev=node
            self.head=node
    def insertAtEnd(self,data):
        if self.head==None:
            self.insertAtStart(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data,itr,None)
        itr.next=node
               
            
    def printdll(self):
        itr=self.head
        emp=""
        while itr:
            emp+=str(itr.data)+"-->"
            itr=itr.next
        print(emp)
    def reverselist(self):
        if self.head==None:
            raise Exception("no values")
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            emp=""
            itrr=itr
            while itrr:
                emp+=str(itrr.data)+"-->"
                itrr=itrr.prev
            print(emp)
    def getlen(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    def delete(self,pos):
        if pos==0:
            itr=self.head
            self.head=itr.next
        if pos<0 or pos>self.getlen():
            raise Exception("invalid range")
        else:
            count=0
            itr=self.head
            while itr:
                if count==pos-1:
                    node=itr.next.next
                    node.prev=itr
                    itr.next=node
                itr=itr.next
                count+=1
    def insertatval(self,pos,data):
        if pos<0 or pos>self.getlen():
            raise Exception("invalid")
        if pos==0:
            self.insertAtStart(data)
        else:
            count=0
            itr=self.head
            while itr:
                if count==pos-1:
                    node=Node(data,itr,itr.next)
                    node1=itr.next
                    itr.next=node
                    node1.prev=node
                itr=itr.next
                count+=1 
    def search(self,key):
        itr=self.head
        count=0
        while itr:
            if key==itr.data:
                print(f"item found at index value {count}")
            itr=itr.next
            count+=1


dll = DoublyLinkedList()
dll.insertAtEnd(34)
dll.insertAtStart(1)    
dll.insertAtStart(2)
dll.insertAtEnd(14)
dll.insertAtEnd(345)
dll.insertAtStart(45)
dll.reverselist()
print(dll.getlen())
dll.delete(4)
dll.reverselist()
# dll.delete(1)
    
# dll.delete(0)
dll.insertatval(1,40)
dll.insertatval(1,15)
dll.insertatval(3,100)
dll.insertatval(0,12)
# dll.insertAtEnd(5)
dll.search(45)
dll.printdll()