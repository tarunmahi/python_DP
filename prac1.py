class value:
    def __init__(self,num1):
        self.num1=num1
    
    def power(self,num2,num3):
        self.num2=num2
        self.num3=num3
        return self.num1+num2+num3
    
        
var=value(5)
print(var.power(5,5))
