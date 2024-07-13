'''Anagrams
Write a program that takes a word and a list of possible anagrams and selects
the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists",
"google", "inlets", and "banana", the program should return a list containing
"inlets". Please read the test suite for the exact rules of anagrams.'''

class Anagram:

    def __init__(self, anagram) -> None:
        self.anagram = anagram
        self.comp_value = sorted(list(anagram.casefold()))

    def match(self, possibilities):

        self.possibilities = possibilities
        
        for element in self.possibilities:
            if element.casefold() == self.anagram.casefold():
                self.possibilities.remove(element)

        return list(filter(lambda x: sorted(list(x.casefold())) == self.comp_value, \
                           self.possibilities))
