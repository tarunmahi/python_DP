def longest(seq):
    min_word=min(len(s) for s in values)
    
    for i in range(min_word):
        if(len(set(s[i] for s in seq)))>1:
            return seq[0][:i]
    return seq[0][:min_word]
    




values=["flight","flight","fliame"]
print(longest(values))