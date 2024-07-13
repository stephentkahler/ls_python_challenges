import random

class Robot:

    _all_names = []

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name == None:
            self.give_a_name()
        return self._name

    def reset(self):
        self._name = None

    def give_a_name(self):

        LETTERS = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
        NUMBERS_START = 0
        NUMBERS_END = 9

        while True:
            self._name = random.choice(LETTERS) + \
                            random.choice(LETTERS) + \
                            str(random.randint(NUMBERS_START, NUMBERS_END)) + \
                            str(random.randint(NUMBERS_START, NUMBERS_END)) + \
                            str(random.randint(NUMBERS_START, NUMBERS_END))
        
            if self._name not in Robot._all_names:
                break

        Robot._all_names.append(self._name)
