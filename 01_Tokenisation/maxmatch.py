def maxmatch(sentence, dictionary):
    if not sentence:
        return []
    for i in range(len(sentence), 0, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in dictionary:
            return [first_word] + maxmatch(remainder, dictionary)
    return [sentence[0]] + maxmatch(sentence[1:], dictionary)

def main():
    import sys

    # Load the dictionary
    with open(sys.argv[1], 'r') as f:
        dictionary = set(f.read().splitlines())

    # Tokenize the input sentence
    for line in sys.stdin:
        line = line.strip()
        tokens = maxmatch(line, dictionary)
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()
