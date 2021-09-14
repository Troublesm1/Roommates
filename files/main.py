class Bill:
    """ Object that contains data about a bill, such as the total amount and period of the bill."""

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    """ Creates a roommate(person) who lives in the flat and pays a share of the bill."""

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass

class PdfReport:
    """ Creates a Pdf file that contains data about the flatmates such as their names, their amount and the billing period"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass