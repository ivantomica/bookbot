import sys
from stats import count_book_words
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = count_book_words(book_contents)
    counted_characters = count_characters(book_contents)
    sorted_characters = sort_characters(counted_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
