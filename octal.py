class Octal:
    def __init__(self, decimal) -> None:
        self.decimal = decimal

    def to_decimal(self):

        octal = 0

        for char in self.decimal:
            if not char.isdigit() or char in "89":
                return octal

        for i, digit in enumerate(str(self.decimal)[::-1]):
            value = int(digit) * (8**i)
            octal += value

        return octal