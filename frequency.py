# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Word Frequency
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 3: Arrays & Maps

from operator import itemgetter
import string
import json

# Create a function word_frequencies that takes
# a string filename as a parameter and returns a
# dictionary mapping each word in the text file
# to the total number of times it occurs. All
# letters should be treated as lower case, and both
# punctuation and numbers should be ignored.
# Letters separated by apostrophes should be left together.
# Your solution may use string & file functions.
# Hint: see https://www.techiedelight.com/remove-punctuations-string-python/

def word_frequencies(filename):
    file = open(filename, 'r')
    text = file.read().lower()
    file.close()
    text = text.replace("'", "")
    text = text.replace("—"," ")
    for c in (string.punctuation + string.digits + "\n"):
        text = text.replace(c, ' ')
    d = {}
    for word in text.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k))

def main():
    files = ["pytest"]
    for f in files:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/" + f + ".txt"))
    file = ["austen"]
    for f in file:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/" + f + ".txt"))
    filess = ["turing"]
    for f in filess:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/" + f + ".txt"))

if __name__ == '__main__':
    main()
