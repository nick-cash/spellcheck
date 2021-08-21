# Nick Cash, Oct 2013
import random

DICTIONARY_PATH = "american-english-large"

def mutate_word(word):
    final_word = ''
    isvowel = lambda c: True if c in 'aeiou' else False
    for c in word:
        addc = 1
        if c.isalpha():
            # Chance to mess up vowels
            if isvowel(c) and random.randint(1,2) == 2:
                c = random.choice(['a', 'e', 'i', 'o', 'u'])
            # Chance to capitalize
            if random.randint(1,2) == 2:
                c = c.upper()
            # Add between 1 and 3 of these to the string
            addc = random.randint(1,3)
        for i in range(0, addc):
            final_word += c
    return final_word

if __name__ == "__main__":
    with open(DICTIONARY_PATH, 'r') as f:
        for word in f.readlines():
            print mutate_word(word.lower().strip())
