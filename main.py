from stats import get_text
from stats import get_num_words
from stats import character_count
from stats import sorted_list
import sys

def main ():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        return
    else:
        book = sys.argv[1]
    
    num_words = get_num_words(book)
    text = character_count(get_text(book))
    sort_list = sorted_list(text)


    print_report(book, num_words, sort_list) 

def print_report(book, num_words, sort_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
