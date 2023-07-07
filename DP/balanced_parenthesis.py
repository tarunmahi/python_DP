class seq:
    def isValid(self,seq:str):
        stack=[]
        opening=set("([{")
        closing=set(")]}")
        pair={")":"(","]":"[","}":"{"}
        for x in seq:
            if x in opening:
                stack.append(x)
            if x in closing:
                if not stack:
                    return False
                elif stack.pop()!=pair[x]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False
                
seq1="{[({{}{[]{{}[]}}[{}]})]}"
print(f'whether the value {seq1} is : {seq().isValid(seq1)}')
                