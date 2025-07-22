def get_num_words(text):

    split_text = text.split()
    num_words = len(split_text)
    return num_words

def get_char_counts(text):
    alphabet_dict= {}
    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet_dict:
            alphabet_dict[lower_char] += 1
        else:
            alphabet_dict[lower_char] = 1
    return alphabet_dict

def sort_on(alphabet_dict):
    return alphabet_dict["num"]

def create_new_list(alphabet_dict):
    new_list = []
    new_list += [{"char": char, "num": num} for char, num in alphabet_dict.items()]
    new_list.sort(key=sort_on, reverse=True)
    return new_list