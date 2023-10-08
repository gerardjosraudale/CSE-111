import random



# Lists of determiners, nouns, and verbs
determiners = ["A", "One", "The", "Some", "Many"]
nouns = ["cat", "man", "woman", "girls", "dogs", "men"]
verbs = ["laughed", "eats", "will think", "thought", "run", "will write"]

# Function to get a random determiner
def get_determiner():
    return random.choice(determiners)

# Function to get a random noun
def get_noun():
    return random.choice(nouns)

# Function to get a random verb
def get_verb():
    return random.choice(verbs)

# Function to generate a sentence
def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    return f"{determiner} {noun} {verb}."

# Main function
def main():
    num_sentences = int(input("Enter the number of sentences to generate: "))
    for _ in range(num_sentences):
        sentence = make_sentence()
        print(sentence)

if __name__ == "__main__":
    main()