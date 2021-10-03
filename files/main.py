from fpdf import FPDF

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
    pass
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Bill', border=1, align='C', ln=1)
        # Insert Period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        # Insert name and due amount of first roommate
        pdf.cell(w=100, h=40, txt=roommate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(roommate1.pays(bill, roommate2)), border=1, ln=1)

        pdf.output(self.filename)

the_bill = Bill(amount=120, period='April 2021')
john = Roommate(name='John', days_in_house=20) #You can write this either way
mary = Roommate('Mary', 25) #You can write this either way

print('John pays: ', john.pays(bill=the_bill, roommate2=mary))
print('Mary pays: ', mary.pays(bill=the_bill, roommate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(roommate1=john, roommate2=mary, bill=the_bill)
