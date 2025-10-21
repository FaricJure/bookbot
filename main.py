from stats import word_count, char_count, char_sort
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()

def main(path_to_book):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")

    book_text = get_book_text(path_to_book)

    print("----------- Word Count ----------")

    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    num_chars = char_count(book_text)
    num_chars_sorted = char_sort(num_chars)
    for char, count in num_chars_sorted.items():
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    # two arguments needed to skip main execution
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])
