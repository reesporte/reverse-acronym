"""
my friend tweeted a bunch of random characters
so i thought it would be funny to make a program that would turn it
into an acronym
"""
import json, random, string

class word_cache(object):
    def __init__(self, corpus):
        super(word_cache, self).__init__()
        self.corpus = corpus
        self.cache = {}

    def get_word(self, letter):
        """
        checks if we've already put the words with those letters in the
        cache, if yes, then just return a random choice from that section of the
        cache, if not then add it to the cache
        """
        if letter not in self.cache.keys():
            things = [x for x in self.corpus['nouns'] if x.lower()[0] == letter]
            self.cache[letter] = things
        else:
            things = self.cache[letter]
        return random.choice(things).capitalize()

    def acronym_getter(self, acronym):
        """
        for each letter in the acronym, get a random word
        """
        acronym = ''.join([x for x in acronym if x.isalpha()])
        final = ""
        for letter in acronym:
            final += self.get_word(letter) + " "

        return final

def main():
    with open('words.json', 'r') as words:
        corp = json.load(words)

    corpus = word_cache(corp)

    x = input("enter acronym: \n>> ")
    while x != 'stop':
        print(corpus.acronym_getter(str(x)))
        x = input("\nenter acronym: \n>> ")

if __name__ == '__main__':
    main()
