class Diamond:

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def make_diamond(cls, letter):
        cls.letter = letter
        cls.find_position()
        cls.create_iterable()
        cls.create_lines()
        cls.print_lines()

    @classmethod
    def find_position(cls):
        cls.position = cls.alphabet.find(cls.letter)

    @classmethod
    def  create_iterable(cls):
        cls.top_iterable = cls.alphabet[:cls.position + 1]
        cls.middle = cls.letter
        cls.botton_iterable = cls.top_iterable[-2::-1]

    @classmethod
    def create_lines(cls):

        cls.top_store = []

        for i, letter in enumerate(cls.top_iterable):

            spacing = ((i * 2) - 1) * " "
            indent = (len(cls.top_iterable) - i - 1) * " "

            if i == 0:
                cls.top_store.append(f"{indent}{letter}{indent}\n")
            else:
                cls.top_store.append(f"{indent}{letter}{spacing}{letter}{indent}\n")

        cls.bottom_store = cls.top_store[-2::-1]

    @classmethod
    def print_lines(cls):

        '''for item in cls.top_store:
            print(item)
        for item in cls.bottom_store:
            print(item)'''
        
        print_list = cls.top_store + cls.bottom_store
        output = "".join(print_list)
        print(output)

Diamond.make_diamond("C")