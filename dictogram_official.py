from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, string, utility, random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, source=None):
        words_list = utility.cleanse(source)
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.random_sent = ["START"]
        # Count words in given list, if any
        # if words_list is not None:
        #     for word in words_list:
        #         self.add_count(word)

        for ind, word in enumerate(words_list):
            if word in self:
                self[word][0] += 1
                try:
                    if words_list[ind + 1] in self[word][1]:
                        self[word][1][words_list[ind + 1]] += 1
                        self[word][2] += 1
                    else:
                        self[word][1][words_list[ind + 1]] = 1
                        self[word][2] += 1
                except:
                    pass
            else:
                self[word] = [1, {}]
                try: 
                    self[word][1][words_list[ind + 1]] = 1
                    self[word].append(1)
                except:
                    pass

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]
        else:
            return 0
    
    def count_to_possibility(self):
        for value in self.values():
            prev_next_val = 0
            for key_next, value_next in value[1].items():
                value[1][key_next] = value_next/value[2]+prev_next_val
                prev_next_val = value[1][key_next]

    def sample(self):
        prev_word = self.random_sent[len(self.random_sent)-1]
        chance = random.random()
        prev_val = 0
        choice = ""
        for key, value in self[prev_word][1].items():
            if chance < value and chance > prev_val:
                choice = key
                break
            prev_val = self[prev_word][1][key]
        return choice

    def get_sentence(self):
        next = ""
        while next != "STOP":
            next = self.sample()
            if next != "START":
                self.random_sent.append(next)
    
    def print_sentence(self):
        # print(" ".join(self.random_sent[1:len(self.random_sent)-1]))
        return " ".join(self.random_sent[1:len(self.random_sent)-1])

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) == 1:
        words = utility.read(arguments[0])
        words = utility.cleanse(words)
        histogram = Dictogram(words)
        histogram.count_to_possibility()
        histogram.get_sentence()
        print(histogram.print_sentence())
        # Test histogram on given arguments
        # print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()