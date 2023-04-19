# classes and objects

class myval:
    var="tarun"

x=myval()
y=myval()

y.var="mohan"

print(x.var)
print(y.var)

##init function

class val:
    
    def __init__(self,number,name):
        self.number=number
        self.name=name
    
    def retnumber(self):
        print("hello mr %s"%self.name)
        return self.number
var=val(7,"tarun")
print(var.retnumber())

#dictionaries 
pairage={"tarun":20,"mohan":30,"mishra":60}

pairage.pop("mohan")
for name,age in pairage.items():
    print("Mr %s has an age of %d"%(name,age))