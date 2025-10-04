from stats import get_book_text
from stats import count_words
from stats import count_char
from stats import sort_dict


def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    text_count = count_words(file_contents)
    char_count = count_char(file_contents)
    sorted_dict = sort_dict(char_count)
    # print(f"Found {text_count} total words")
    # print(char_count)
    print(f"Sorted dict: {sorted_dict}")


main()
