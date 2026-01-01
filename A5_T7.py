DELIMITER = ','  


def collectWords():
    """Collects words from the user until an empty input is given."""
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(words_string):
    """Analyses words: count, total characters, and average word length."""
    if not words_string:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    words = words_string.split(DELIMITER)
    word_count = len(words)
    char_count = sum(len(w) for w in words)
    average = char_count / word_count

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print(f"- {average:.2f} Average word length")


def main():
    """Main program logic."""
    print("Program starting.")
    collected = collectWords()
    analyseWords(collected)
    print("Program ending.")



main()