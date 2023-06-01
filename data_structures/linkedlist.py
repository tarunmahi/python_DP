class node:
    def __init__(self):
        self.value=0
        self.next=None
        
head=None
one=None
two=None
three=None

one=node()
two=node()
three=node()

one.value=1
two.value=2
three.value=50

one.next=two
two.next=three
three.next=None

head=one
while(head!=None):
    print("->"+str(head.value))
    head=head.next
    

