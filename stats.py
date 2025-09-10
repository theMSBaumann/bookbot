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


def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    d_list = []
    for item in dict:
        temp_dict = {"char": "", "num": ""}
        temp_dict["char"] = item 
        temp_dict["num"] = dict[item]
        d_list.append(temp_dict)
    d_list.sort(reverse=True, key=sort_on)
    return d_list



print(sort_dict({
    "Mercury": 57.91,
    "Venus": 108.2,
    "Earth": 149.6
}))