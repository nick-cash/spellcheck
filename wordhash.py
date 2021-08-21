from solution import word_hash

while True:
    try:
        word = raw_input("> ").lower()
        print "Word: %s" % word
        print "Word hash: %s" % word_hash(word)
    except (EOFError):
        break