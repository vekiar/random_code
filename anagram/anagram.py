from random import randint
import sys

if (len(sys.argv) < 2): sys.exit("You must provide at least 1 argument.")

def remove_char(char, word):
    out = ""
    removed = False
    for c in word:
        if c != char:
            out += c
        elif c == char and removed:
            out += c
        else:
            removed = True
    return out

word = sys.argv[1]
print("%s" % (word))
anagram = ""
random_char = word[randint(0,len(word) - 1)]
anagram += random_char
word = remove_char(random_char, word)
while len(word) > 0:
    random_char = word[randint(0, len(word) - 1)]
    anagram += random_char
    word = remove_char(random_char, word)

print("%s" % (anagram))