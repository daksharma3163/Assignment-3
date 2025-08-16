def toggle_cast_count(s):
    toggled = ""
    counts = {'upper':0,'lower':0}
    for char in s:
        if(char.isupper()):
            counts['upper'] += 1
            toggled += char.lower()
        else:
            counts['lower'] += 1
            toggled += char.upper()
    
    return counts, toggled
        

counts_dict, toggled_word = toggle_cast_count("HeLLo")
for key, value in counts_dict.items():
    print(f"{key} => {value}")

print(f"Toggled Word => {toggled_word}")