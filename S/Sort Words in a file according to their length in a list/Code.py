def create_dict(file_path):
    with open(file_path, 'r') as f:
        paragraph = f.read()

    words = paragraph.split()
    word_dict = {}
    for word in words:
        word_length = len(word)
        if word_length not in word_dict:
            word_dict[word_length] = []
        word_dict[word_length].append(word)
    return word_dict

file_path = input("Enter the file path: ")
word_dict = create_dict(file_path)
print("Dictionary with word length as key and words with that length as value:")
print(word_dict)
