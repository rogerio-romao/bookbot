def main():
    file_contents = open_file("books/frankenstein.txt")
    words = count_words(file_contents)
    letters = dict_letters(file_contents)
    letters_list = []
    for letter in letters:
        letters_list.append({letter: letters[letter]})

    sorted_letters = sort_letters(letters)
    filtered_letters = list(filter(filter_letters, sorted_letters))
    print_results(words, filtered_letters)

def open_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def dict_letters(file_contents):
    letters = {}
    for letter in file_contents.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_letters(letters):
    return sorted(letters.items(), key=lambda x: x[1], reverse=True)

def filter_letters(letters):
    return letters[0].isalpha()

def print_results(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("\n")
    for letter in letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

main()