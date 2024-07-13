class RomanNumeral:

    NUMERALS = {"M": 1000,
                "CM": 900,
                "D": 500,
                "CD": 400,
                "C": 100,
                "XC": 90,
                "L": 50,
                "XL": 40,
                "X": 10,
                "IX": 9,
                "V": 5,
                "IV": 4,
                "I": 1,
                }
    
    def __init__(self, number) -> None:
        self.number = number
        self.output = ""

    def to_roman(self):
        for key, value in RomanNumeral.NUMERALS.items():
            while self.number >= value:
                self.output += key
                #print(key)
                self.number -= value
                #print(value)
            
        return self.output


