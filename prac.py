def longest_common_prefix(seq):
    min_len=min(len(s) for s in seq) 
    
    for i in range(min_len):
        if(len(set(s[i] for s in seq)))>1:
            return seq[0][:i]
    return seq[0][:min_len]

words = ["apple", "appa", "application"]
common_prefix = longest_common_prefix(words)
print(common_prefix)