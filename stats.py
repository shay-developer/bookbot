def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(text_content):
    text_array = text_content.split(" ")
    text_count = len(text_array)
    return text_count


def count_char(text_content):
    text_array = text_content.split()
    words = set()
    char_dict = {}
    for word in text_array:
        for char in word:
            char.lower()
            if char not in words:
                char_dict[char] = 0
                char_dict[char] += 1
            else:
                char_dict[char] += 1
            words.add(char)

    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(dict):
    sorted_dicts = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        sorted_dicts.append(new_dict)
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
