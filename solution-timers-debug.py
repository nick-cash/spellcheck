import difflib, functools, time
from collections import defaultdict

DICTIONARY_PATH = "american-english-large"
DISPLAY_TIMERS = True

letter_hash = lambda w: w[0] if not w[0] in 'aeiou' else '~'

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self
    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def translate(word):
    translation = ''
    last_hashc = ''
    for c in word:
        hashc = letter_hash(c)
        if last_hashc == hashc:
            continue
        else:
            translation += letter_hash(c) + ':'
        last_hashc = hashc

    return translation

def get_best_match(word, debug=False):
    wordset = dictionary[letter_hash(word)][translate(word)]
    matches = difflib.get_close_matches(word, wordset, 3, 0.1)

    if debug:
        print "Wordset = ",
        print wordset
        print "Word: %s, Translation: %s" % (word, translate(word))
        if matches:
            print "Match: %s, Translation: %s" % (matches[0], translate(matches[0]))

    return matches[0] if matches else "NO SUGGESTION"

# Load dictionary
with Timer() as t:
    dictionary = defaultdict(lambda: defaultdict(set))
    with open(DICTIONARY_PATH) as f:
        for word in f.readlines():
            word = word.lower().strip()
            dictionary[letter_hash(word)][translate(word)].add(word)

print "Loaded dictionary in %.05f seconds." % t.interval

# Check words
while True:
    word = raw_input("> ").lower()
    with Timer() as t:
        result = get_best_match(word)

    output = result
    if DISPLAY_TIMERS:
        output += " (%0.05fs)" % t.interval
    print output
