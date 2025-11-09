def count_words_in_string(string):
    words_list = string.split()
    words_count = len(words_list)
    return words_count


def count_unique_characters(string):
    string_lowercase = string.lower()
    characters = {}
    for character in string_lowercase:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def sort_on(items):
    return items["num"]


def sort_dictionary(characters):
    new_list = []
    for item in characters:
        line = {"char": item, "num": characters[item]}
        new_list.append(line)

    new_list.sort(key=sort_on, reverse=True)
    return new_list
