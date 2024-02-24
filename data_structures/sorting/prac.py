class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LL:
    def __init__(self):
        self.head=None
    def insert_bi(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_end(self,data):
        if self.head==None:
            self.insert_bi(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def insert_pos(self,data,pos):
        if pos<0 and pos>self.getlen():
            raise Exception("invalid range")
        if pos==0:
            self.insert_bi(data)
            return
        else:
            count=0
            itr=self.head
            while itr:
                if count==pos-1:
                    node=Node(data,itr.next)
                    itr.next=node
                itr=itr.next
                count+=1
                
                
    def remove(self,pos):
        if pos<0 and pos>self.getlen():
            raise Exception("invalid range")
        count=0
        itr=self.head
        while itr:
            if count==pos-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
    def getlen(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def print(self):
        itr=self.head
        emp=""
        while itr:
            emp+=str(itr.data)+"-->"
            itr=itr.next
        print(emp)
    
    
    
ll=LL()
ll.insert_bi(24)
ll.insert_bi(12)
ll.insert_end(90)
ll.insert_bi(5)
ll.insert_end(13)
ll.print()
ll.remove(3)
ll.insert_pos(50,3)
ll.print()
print(ll.getlen())