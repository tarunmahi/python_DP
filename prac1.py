class seq:
    def isValid(self,seq):
        opening=set("([{")
        closing=set(")}]")
        pair={')':'(',"}":"{","]":"["}
        stack=[]
        
        for i in seq:
            if i in opening:
                stack.append(i)
            if i in closing:
                if not stack:
                    return False
                elif stack.pop()!=pair[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False
       
seq1="{{}[({([]({}))})]}"        
print(f"is the value {seq1} really {seq().isValid(seq1)}")
                
                 