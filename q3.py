def is_isogram(word):
    word = word.lower()
    seen = {}
    for char in word:
        if char in seen:
            return False
        seen[char] = True
    return True


word = input("Enter a word: ")
is_isogram(word)