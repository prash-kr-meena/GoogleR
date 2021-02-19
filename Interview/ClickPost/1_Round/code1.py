def joinWords(words):  # For simplicity assume that each string is of the same length x, and therea re n strings
    sentence = ""
    for word in words:
        sentence = sentence + word
    return sentence

# What is the time complexity of this code,
# In terms of words  -> my answer o(n)
# and In terms of characters -> my answer o(n2)
