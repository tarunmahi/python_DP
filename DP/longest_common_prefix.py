
def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the minimum length string among all the input strings
    min_length = min(len(s) for s in strings)

    # Iterate over the characters up to the minimum length
    for i in range(min_length):
        # Check if all characters at index i are the same
        if len(set(s[i] for s in strings)) > 1:
            return strings[0][:i]  # Return the prefix up to index 

    return strings[0][:min_length]  # Return the entire minimum length string


# Example usage:
words = ["apple", "appa", "application"]
common_prefix = longest_common_prefix(words)
print(common_prefix)