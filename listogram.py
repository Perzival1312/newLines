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
    histogram = []
    for j in range(len(source)):
        contains = False
        if len(histogram) == 0:
            histogram.append([source[j], 1])
        else:
            for i in range(len(histogram)):
                if source[j] == histogram[i][0]:
                    histogram[i][1] += 1
                    contains = True
            if not contains:
                histogram.append([source[j], 1])
    return histogram

# def unique_words(histogram):
#     unique_word_counter = 0
#     for 

histogram = make_histogram(words_list)
print(histogram)