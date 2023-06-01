class Sum:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def addition(self,variable1):
        return self.num2+self.num1+variable1
    
var=Sum(5,10)

print(var.addition(5))