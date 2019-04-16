import random, sys
from collections import Counter

f = open("/usr/share/dict/words", "r")
words_list = f.readlines()
f.close()
word_count = sys.argv[1:]
final_words = []
try:  # get random words from dict
    int(word_count[0])
    for _ in range(int(word_count[0])):
        final_words.append(random.choice(words_list))
except:  # get words from dict starting wiht a certain string
    word_fragment = word_count[0]
    for words in words_list:
        temp_word = words[: len(word_fragment)]
        if temp_word == word_fragment:
            final_words.append(words)
print("".join(final_words))

# Real Anagrams
def real_anagram_gen():
    anagram_results = []
    for words in words_list:
        word = words[:-1]
        if Counter(word_count[0]) == Counter(word):
            anagram_results.append(word)
        print(anagram_results)
