from stats import word_counter
from stats import char_counter
from stats import freq_sorter
from stats import print_sorted
import sys # sys.argv[index of argument]- used when calling the program with specific arguemnts such as python3 main.py[first - argv[0]] <path_of_book>[so argv[1]]
# path_to_book = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) != 2: #if the number of arguments does not match, then the program exits and explains how to properly run it
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1) 


    book_text = get_book_text(sys.argv[1])
    counted_words = word_counter(book_text)
    counted_chars = char_counter(book_text)
    sorted_freq = freq_sorter(counted_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    print_sorted(sorted_freq)
    print("============= END ===============")
main()