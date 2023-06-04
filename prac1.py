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
            node=Node(data)
            self.head.prev=node
            node.next=self.head
            self.head=node
    
    def insertAtEnd(self,data):
        if self.head==None:
            self.insertAtStart(data)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(data)
            itr.next=node
            node.prev=itr
    def delete(self,pos):
        if pos<0 or pos>self.getlength():
            raise Exception("invalid")
        if pos==0:
            self.head=self.head.next
        else:
            itr=self.head
            count=0
            while itr:
                if count==pos-1:
                    if itr.next:
                        itr.next=itr.next.next
                        if itr.next:
                            itr.next.prev=itr
                itr=itr.next
                count+=1        
    
    def printdll(self):
        itr=self.head
        if self.head==None:
            raise Exception("empty List")
        emp=""
        while itr:
            emp+=str(itr.data)+"-->"
            itr=itr.next
        print(emp)
    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insertatval(self,pos,val):
        if pos==0:
            self.insertAtStart(val)
        else:
            count=0
            itr=self.head
            node=Node(val)
            while itr:
                if count==pos-1:
                    node.prev=itr
                    node.next=itr.next
                    itr.next=node
                    itr.next.prev=node
                    """
                    node.next=itr.next
                    node.prev=itr
                    itr.next=node
                    itr.next.prev=node
        """
                count+=1
                itr=itr.next





if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(34)
    dll.insertAtStart(45)
    dll.printdll()

    dll.delete(3)
    dll.delete(1)
    
    dll.delete(0)
    dll.printdll()
    
    dll.insertatval(1,40)
    dll.insertatval(1,15)
    dll.insertatval(3,100)
    dll.insertatval(0,12)

   
    dll.printdll()
    