class seq:
    def isValid(self,seq:str):
        stack=[]
        opening=set("[{(")
        closing=set(")}]")
        mapping={')':'(','}':'{',']':'['}
        for i in seq:
            if i in opening:
                stack.append(i)
            if i in closing:
                if not stack:
                    return False
                elif stack.pop()!=mapping[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False
sequence = '{}[{]}'
print(f'is the {sequence} a valid one :  {seq().isValid(sequence)}')