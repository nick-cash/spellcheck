# Nick Cash, Oct 2013
from difflib import get_close_matches
from collections import defaultdict

DICTIONARY_PATH = "american-english-large"

letter_hash = lambda c: c[0] if not c[0] in 'aeiou' else '~'

def word_hash(word):
    hash_str = ''
    last_hashc = ''
    for c in word:
        hashc = letter_hash(c)
        if last_hashc == hashc:
            continue
        else:
            hash_str += hashc
        last_hashc = hashc
    return hash_str

def get_best_match(word, dictionary):
    matches = get_close_matches(word, dictionary[word_hash(word)], 3, 0.01)
    return matches[0] if matches else "NO SUGGESTION"

if __name__ == "__main__":
    # Load dictionary
    dictionary = defaultdict(set)
    with open(DICTIONARY_PATH, 'r') as f:
        for word in f.readlines():
            word = word.lower().strip()
            dictionary[word_hash(word)].add(word)
    # Check words
    while True:
        try:
            word = raw_input("> ").lower()
            if len(word) > 0:
                print get_best_match(word, dictionary)
        except (EOFError):
            break
