def count_words(text):
    words = text.split()
    return len(words)

def main():

    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)
    word_count = count_words(file_contents)
    print(f"Total number of words in the book: {word_count}")

if __name__ == "__main__":
    main()