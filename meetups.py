from datetime import date

class Meetup:
    def __init__(self, year, month):
        self.date = date(year, month)

    def day(self, day, nth):
        
        options = ["first", "second", "third", "fourth", "fifth", "last"]
