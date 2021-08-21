Note: Solution was written and tested with Python 2.7.3

------------------------------------------
- Solution Description & Time Complexity -
------------------------------------------

Each word from the dictionary is hashed and inserted into a chained hashtable
which uses sets. Some analysis shows that, when using the 'american-english-large'
dictionary, we have 129,235 keys. 112,034 of those keys are single word sets. That
means we have amortized O(1) performance for most searches. The remaining 17,201
keys have two or more words in its set with the highest number of words being
35 for the key 'd~n~' (keys explained below). We use the function get_close_matches
from Python's standard difflib to find the best word amongst chains. According
to the documentation, the SequenceMatcher that does the comparisons is O(n^2) in
the worst case, and O(n) in the best case. This gives the implementation's best
and most common case O(1) performance; our worst case is between O(n) and O(n^2)
where n is the number of words in a chain (max 35 for the 'american-english-large' dictionary).

The hash is what implements the search behavior for this spell checker. We are
on the lookout for repeated letters, incorrect vowels, and case problems. To
handle these we lowercase everything, remove repeated letters, and change all
vowels into the tilde character '~'. This means words that are misspelled with
these problems should be hashed the same as normal words. We then pick our word by
taking the word in the chain that is rated as most similar to the input word as
determined by the algorithm in SequenceMatcher which finds the longest continuous
matching subsequence.

SequenceMatcher Docs: http://docs.python.org/2/library/difflib.html#difflib.SequenceMatcher


-------------------------------
- Error Generator and Testing -
-------------------------------

The generator.py script will read in a dictionary and print out a mutation of each
word. The mutation is randomly capitalized, vowels are randomly changed, and each
character can be added between 1 and 3 times (save punctuation). This can be piped
to a file or to the solution.py script directly.

Since they operate on the same dictionary, it is possible to do something like this:

python error_generator.py > errors.txt
python solution.py < errors.txt > corrections.txt

Then you can open up the dictionary, errors, and corrections side by side. Each line
corresponds exactly, so you can see the original word, the mutated version, and the suggested
correction for each word in the dictionary. You can also easily verify that there
are no 'NO SUGGESTION' outputs.

You can, of course, run solution.py interactively.