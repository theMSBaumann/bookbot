import sys
from stats import (
    count_words,
    count_characters, 
    sort_dict
)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    check_input()
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    characters = count_characters(text)
    sorted_chars = sort_dict(characters) 
    print_report(book_path, num_words, sorted_chars)


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def check_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



        




main()
    

