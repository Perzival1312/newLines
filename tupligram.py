import sys, string
string.punctuation += "”“’‘—"

f = open(str(sys.argv[1:][0]), 'r')
word_list = f.readlines()
f.close()

histogram = []
words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()

def make_histogram(source):
    histogram = [(),()]
    for index, words in enumerate(source):
        count = 0
        if words not in histogram:
            for checking in source[index:]:
                if words == checking:
                    count += 1
            histogram += (words, count)
    return histogram

# def unique_words(histogram):
#     unique_word_counter = 0
#     for 

histogram = make_histogram(words_list)
print(type(histogram))
