from stats import count_unique_characters, count_words_in_string, sort_dictionary


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_file = "./books/frankenstein.txt"
    book_text = get_book_text(book_file)
    book_words = count_words_in_string(book_text)
    character_count = count_unique_characters(book_text)
    sorted_characters = sort_dictionary(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for char in sorted_characters:
        if char["char"].isalpha():
            print(f" {char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
