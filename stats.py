def count_book_words(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(items):
    return items["num"]

def count_characters(file_contents):
    lowercase_contents = file_contents.lower()
    count = {}

    for character in lowercase_contents:
        if character.isalpha():
            count[character] = count.get(character, 0) + 1

    return count

def sort_characters(characters):
    sorted_list = []

    for character in characters:
        sorted_list.append({
            "char" : character,
            "num" : characters[character]
        })

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
