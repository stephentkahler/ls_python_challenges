class PerfectNumber:

    @classmethod
    def classify(cls, number):
          
        cls.number = number
        cls.perfect_abundant_deficient = None

        cls.check_positive()
        cls.get_divisiors()
        cls.sum_divisors()
        cls.determine()
        return cls.perfect_abundant_deficient

    @classmethod
    def check_positive(cls):
        if cls.number <= 0:
            raise ValueError("Input must be a positive integer")        

    @classmethod
    def get_divisiors(cls):
        cls.divisors = []
        for counter in range(1,cls.number):
            if cls.number % counter == 0:
                cls.divisors.append(counter)

    @classmethod
    def sum_divisors(cls):
        cls.sum = sum(cls.divisors)

    @classmethod
    def determine(cls):
        if cls.sum < cls.number:
            cls.perfect_abundant_deficient = "deficient"
        elif cls. sum > cls.number: 
            cls.perfect_abundant_deficient = "abundant"
        else:
            cls.perfect_abundant_deficient = "perfect"