'''Triangles
Write a program to determine whether a triangle is
equilateral, isosceles, or scalene.

    *An equilateral triangle has all three sides the same length.
    *An isosceles triangle has exactly two sides of the same length.
    *A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0,
and the sum of the lengths of any two sides must be greater than the length of
the third side.'''

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.sides = [side_1, side_2, side_3]
        if not self._is_triangle():
            raise ValueError("Lengths Cannot Create Triangle")
        if not self._positive():
            raise ValueError("All side lenghts must be positive")

        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    @property
    def kind(self):
        if self.side_1 == self.side_2 == self.side_3:
            return "equilateral"
        elif self.side_1 == self.side_2  \
            or self.side_1 == self.side_3 \
            or self.side_2 == self.side_3:
            return "isosceles"
        else:
            return "scalene"
        
    def _is_triangle(self):
        return (self.sides[0] + self.sides[1] > self.sides[2]) \
            and (self.sides[0] + self.sides[2] > self.sides[1]) \
            and (self.sides[1] + self.sides[2] > self.sides[0])

    def _positive(self):
        return self.sides[0] > 0 and self.sides[1] > 0 and self.sides[2] > 0