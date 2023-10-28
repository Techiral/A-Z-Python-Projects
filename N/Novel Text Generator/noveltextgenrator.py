import random

def build_markov_chain(text, order=2):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])
        next_word = words[i + order]
        
        if prefix in markov_chain:
            markov_chain[prefix].append(next_word)
        else:
            markov_chain[prefix] = [next_word]
    
    return markov_chain

def generate_text(markov_chain, length=100, seed=None):
    if seed is None:
        seed = random.choice(list(markov_chain.keys()))
    
    current_prefix = list(seed)
    generated_text = current_prefix
    
    for _ in range(length):
        next_word = random.choice(markov_chain[tuple(current_prefix)])
        generated_text.append(next_word)
        current_prefix = current_prefix[1:] + [next_word]
    
    return ' '.join(generated_text)

# Example usage
if __name__ == "__main__":
    with open('your_novel_source.txt', 'r') as file:
        source_text = file.read()

    order = 2  # Adjust the order as needed
    markov_chain = build_markov_chain(source_text, order)

    generated_text = generate_text(markov_chain, length=200)
    print(generated_text)
