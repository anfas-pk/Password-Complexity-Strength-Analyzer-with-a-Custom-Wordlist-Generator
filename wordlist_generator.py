from itertools import permutations, product

class WordlistGenerator:
    def generate(self, base_words, max_length=3):
        wordlist = set()
        for i in range(1, max_length+1):
            for combo in product(base_words, repeat=i):
                wordlist.add(''.join(combo))
        return sorted(wordlist)
