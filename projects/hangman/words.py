def list_val(seq):
    list1=["(","[","{"]
    list2=[")","}","]"]
    pair={')':'(',']':'[','}':'}'}
    stack=[]
    for i in seq:
        if i in list1:
            stack.append(i)
        elif i in list2:
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