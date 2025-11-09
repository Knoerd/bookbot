import sys

from stats import count_unique_characters, count_words_in_string, sort_dictionary


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    book_words = count_words_in_string(book_text)
    character_count = count_unique_characters(book_text)
    sorted_characters = sort_dictionary(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for char in sorted_characters:
        if char["char"].isalpha():
            print(f" {char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
