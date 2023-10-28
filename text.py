import random

# Define lists of words and phrases to use in the generator
nouns = ["cat", "dog", "house", "car", "book"]
verbs = ["runs", "jumps", "sleeps", "eats", "reads"]
adjectives = ["happy", "fast", "green", "loud", "big"]
adverbs = ["quickly", "loudly", "slowly", "gently", "suddenly"]

def generate_random_text():
    sentence = f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} {random.choice(adjectives)}."
    return sentence

# Generate and print random text
for _ in range(5):
    random_text = generate_random_text()
    print(random_text)
