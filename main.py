def CountWords(text):
    words = file_contents.split()
    return len(words)


def CountCharacters(text):
    lower = text.lower()
    char_count = {}
    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def PrintBookReport(text):
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = CountWords(text)
    print(f"{word_count} words found in the document")
    print()
    char_counts = list(CountCharacters(text).items())
    char_counts.sort(key=lambda char_count: char_count[1], reverse=True)
    for char_count in char_counts:
        if char_count[0].isalpha():
            print(f"The '{char_count[0]}' character was found {char_count[1]} times")
    print("--- End report ---")


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    PrintBookReport(file_contents)
