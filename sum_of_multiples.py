'''Sum of Multiples
Write a program that, given a natural number and a set of one or more other
numbers, can find the sum of all the multiples of the numbers in the set that
are less than the first number. If the set of numbers is not given,
use a default set of 3 and 5.

For instance, if we list all the natural numbers up to, but not including,
20 that are multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.
The sum of these multiples is 78.'''

class SumOfMultiples:
    def __init__(self, *args) -> None:

        if len(args) < 1:
            self.other_nums = (3,5)
        else:
            self.other_nums = set(args)

    @classmethod
    def sum_up_to(cls, natural_number):

        return cls().to(natural_number)

    def to(self, natural_number):

        self.multiples = []

        for i in range(natural_number):
            for num in self.other_nums:
                if i % num == 0:
                    self.multiples.append(i)

        return sum(set(self.multiples))