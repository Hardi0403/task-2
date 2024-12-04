import random
from nltk.corpus import wordnet

def generate_shadow_sentence(character_length):


    sentence = "This is a sample sentence to demonstrate the function."

    words = sentence.split()
    shadow_words = []

    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            random_synonym = random.choice(synonyms).lemmas()[0].name()
            shadow_words.append(random_synonym)
        else:
            shadow_words.append(word)

    shadow_sentence = " ".join(shadow_words)

    # Truncate the sentence to the desired character length
    truncated_sentence = shadow_sentence[:character_length]

    return truncated_sentence