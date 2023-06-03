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
            return
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
            node=Node(data)
            while itr.next:
                itr=itr.next
            itr.next=node
            node.prev=itr.next
    def printdll(self):
        if self.head==None:
            print("the list is empty")
        else:
            itr=self.head
            emp=""
            while itr:
                emp+=str(itr.data)+"-->"
                itr=itr.next
            print(emp)
                
    def delete(self,pos):
        if pos<0 or pos>self.getlen():
            raise Exception("invalid range is given here")
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
                            break
                itr=itr.next
                count+=1
                    
                    
    def getlen(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count







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