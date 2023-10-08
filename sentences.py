import random

# Lists of determiners, nouns, verbs, and prepositions
determiners = ["A", "One", "The", "Some", "Many"]
nouns = ["cat", "man", "woman", "girls", "dogs", "men"]
verbs = ["laughed", "eats", "will think", "thought", "run", "will write"]
prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

# Function to get a random determiner
def get_determiner():
    return random.choice(determiners)

# Function to get a random noun
def get_noun():
    return random.choice(nouns)

# Function to get a random verb
def get_verb():
    return random.choice(verbs)

# Function to get a random preposition
def get_preposition():
    return random.choice(prepositions)

# Function to generate a prepositional phrase
def get_prepositional_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

# Function to generate a sentence
def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase1 = get_prepositional_phrase()
    prepositional_phrase2 = get_prepositional_phrase()
    return f"{determiner} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."

# Main function
def main():
    num_sentences = int(input("Enter the number of sentences to generate: "))
    for _ in range(num_sentences):
        sentence = make_sentence()
        print(sentence)

if __name__ == "__main__":
    main()
