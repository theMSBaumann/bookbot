def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lc_text = text.lower()
    character_dict = {}
    print(lc_text)
    for char in lc_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict



