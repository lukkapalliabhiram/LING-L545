# extract_dictionary.py
import sys

def extract_unique_words(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
        words = set(text.split())
    return words

if __name__ == "__main__":
    filename = sys.argv[1]
    dictionary = extract_unique_words(filename)
    with open("dictionary.txt", 'w', encoding="utf-8") as f:
        for word in dictionary:
            f.write(word + "\n")
