"""
Word Occurrence Counter
Estimated time to complete: 20 minutes
"""

def main():
    text = input("Text: ")
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort the words
    sorted_words = sorted(word_counts.keys())

    # Find the longest word for alignment
    max_length = max(len(word) for word in sorted_words)

    # Print the formatted output
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()
