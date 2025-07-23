def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_book):
    words = get_book_text(path_to_book).split()
    num_words = len(words)
    return num_words

def get_num_chars(path_to_book):
    dict_char = {}
    words = get_book_text(path_to_book).split()
    for word in words:
        lower_word = word.lower()
        for character in lower_word:
            if not character in dict_char:
                dict_char.update({character:1})
            else:
                current_val = dict_char[character]
                new_val = current_val + 1
                dict_char.update({character:new_val})

    return dict_char

def sort_on(items):
    return items["num"]

def sorted_list_of_dictionaries(unsorted_dictionary):
    sorted_list = []
    for key in unsorted_dictionary:
        sorted_list.append({"char":key, "num":unsorted_dictionary.get(key)})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
