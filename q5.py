def reverse_by_words(s):
    word_list = list(map(str, s.split()))
    result = ""
    for word in word_list:
        word = word[::-1]
        result = result + word + " "
    return result

s = input("Enter the text: ")

print(reverse_by_words(s))