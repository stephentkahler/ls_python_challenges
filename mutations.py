'''Point Mutations
Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a
nucleic acid, in particular DNA. Because nucleic acids are vital to cellular
functions, mutations tend to cause a ripple effect throughout the cell. Although
mutations are technically mistakes, a very rare mutation may equip the cell with
a beneficial attribute. In fact, the macro effects of evolution are attributable
to the accumulated result of beneficial microscopic mutations over many
generations.

The simplest and most common type of nucleic acid mutation is a point mutation,
which replaces one base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken
from different genomes with a common ancestor, we get a measure of the minimum
number of point mutations that could have occurred on the evolutionary path
between the two strands.

This is called the Hamming distance.'''

class DNA:
    
    def __init__(self, strand_1) -> None:
        self.strand_1 = strand_1

    def hamming_distance(self, strand_2):
        
        counter = 0

        self.strand_2 = strand_2
        self.fix_lengths()

        for i, point in enumerate(self.strand_1):
            if point != self.strand_2[i]:
                counter += 1

        return counter

    def fix_lengths(self):

        length = min(len(self.strand_1), len(self.strand_2))

        self.strand_1 = self.strand1[:length]
        self.strand_2 = self.strand2[:length]
