class seq:
    def isValid(self,seq:str):
        stack=[]
        opening=set("({[")
        closing=set(")]}")
        pair={")":"(","}":"{","]":"["}
        
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
        
seq1="{[]{{{[()()]}}}}[]"
print(f'is the value {seq1} : {seq().isValid(seq1)}') 