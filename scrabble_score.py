class Scrabble:

    KEY = {
        'AEIOULNRST': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10}

    def __init__(self, word):
        self.word = word if word else ""

    def score(self):

        total = 0

        for letter in self.word:
            for key, value in Scrabble.KEY.items():
                if letter.casefold() in key.casefold():
                    total += value
 
        return total

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()