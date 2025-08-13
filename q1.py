def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

text = "Python programming is powerful" 
print(f"The longest word is: {find_longest_word(text)}")