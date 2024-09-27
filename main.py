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

    word_count = count_words(file_contents)
    print(f"--- Beginn report of {path_to_file} ---")
    print(f"Total number of words in the book: {word_count}")
    print()

    character_count = count_characters(file_contents)
    #print(f"Character frequencies:\n{character_count}")

    sorted_char_count = char_count_sort(character_count)
    for char, count in sorted_char_count.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()