'''Series
Write a program that will take a string of digits and return all the possible
consecutive number series of a specified length in that string.

For example, the string "01234" has the following 3-digit series:
    -012
    -123
    -234
Likewise, here are the 4-digit series:
    -0123
    -1234
Finally, if you ask for a 6-digit series from a 5-digit string,
you should throw an error.'''

class Series:
    
    def __init__(self, number) -> None:
        self.number = number

    def slices(self, slice_length):

        slices = []
        num_list = []

        if slice_length > len(self.number):
            raise ValueError
        
        for char in self.number:
            num_list.append(int(char))

        for i in (range(len(num_list) - slice_length + 1)):
            slices.append((num_list)[i : i+slice_length])

        return slices
    
series = Series("01234")
slices = series.slices(1)
print(slices)