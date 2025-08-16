def compress_consecutive(s):
    if not s:
        return []
    
    count = 1
    compressed = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed += s[i-1] + str(count)
            count = 1
    compressed += s[-1] + str(count)  
    return compressed  


s = input("Enter the text: ")
print(compress_consecutive(s))



