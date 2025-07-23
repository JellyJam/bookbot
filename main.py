import sys

from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list_of_dictionaries

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    total_words = get_num_words(sys.argv[1])
    sorted_list = sorted_list_of_dictionaries(get_num_chars(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for items in sorted_list:
        _char = items.get("char")
        _num  = items.get("num")
        if _char.isalpha():
            print(f"{_char}: {_num}")
    print("============= END ===============")
main()
