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
        pass
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
        pass








if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtStart(45)
   
    dll.printdll()