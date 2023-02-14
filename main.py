book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_occurrences(text)
    report(chars_dict, num_words)

def get_occurrences(text):
    occurrences = {}

    for ch in text:
        ch = ch.lower()
        if not ch in occurrences:
            occurrences[ch] = 0
        occurrences[ch] += 1

    return occurrences

def report(chars_dict, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    sorted_dict = sorted(chars_dict.items(), key = lambda x:x[1], reverse = True) # [ (key, value) ]

    for pair in sorted_dict:
        ch = pair[0]
        num = pair[1]
        if ch.isalpha():
            print(f"The {ch} character was found {num} times")

    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(book_path) as f:
        return f.read()

main()