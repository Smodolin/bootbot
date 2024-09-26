def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def char_count_sort(character_count):
    character_sorted = dict(sorted(character_count.items()))
    return character_sorted

def main():

    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()

    #print(file_contents)

    word_count = count_words(file_contents)
    print(f"Total number of words in the book: {word_count}")

    character_count = count_characters(file_contents)
    print(f"Character frequencies:\n{character_count}")

    sorted_char_count = char_count_sort(character_count)
    print(f"Character sorted: \n{sorted_char_count}")

if __name__ == "__main__":
    main()