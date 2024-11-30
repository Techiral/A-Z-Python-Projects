def word_count(text):
    # Split the text into words using whitespace as the separator
    words = text.split()
    return len(words)

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    count = word_count(input_text)
    print(f"Word count: {count}")
