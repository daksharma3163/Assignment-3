def replace_middle_with_star(s):
    if len(s) <= 2:
        return s
    return s[0] + '*' * (len(s) - 2) + s[-1]

text = input("Enter the word: ")
print(replace_middle_with_star(text)) 
