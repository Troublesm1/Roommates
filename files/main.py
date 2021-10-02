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

    def pays(self, bill, roommate2):
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """ Creates a Pdf file that contains data about the roommates such as their names, their amount and the billing period"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass

the_bill = Bill(amount=120, period='March 2021')
john = Roommate(name='John', days_in_house=20) #You can write this either way
mary = Roommate('Mary', 25) #You can write this either way

print('John pays: ', john.pays(bill=the_bill, roommate2=mary))
print('Mary pays: ', mary.pays(bill=the_bill, roommate2=john))