from fpdf import FPDF
import webbrowser

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

        roommate1_pay = str(round(roommate1.pays(bill, roommate2), 2))
        roommate2_pay = str(round(roommate2.pays(bill, roommate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image('files\house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of first roommate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt= roommate1_pay, border=0, ln=1)

        # Insert name and due amount of second roommate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt= roommate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        #Open PDF file in Default PDF view or browser
        webbrowser.open(self.filename)
        #USE THIS LINE INSTEAD OF LINE 57 IF USING MAC
        # webbrowser.open('file://' + os.path.realpath(self.filename))

amount = float(input('Hey user, enter the bill amount:'))
period = input('What is the bill period: E.g. December 2021: ')

name1 = input('What is your name? ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house during the bill period? '))

name2 = input('What is the name of the other roommate? ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill period? '))


the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1) #You can write this either way
roommate2 = Roommate(name2, days_in_house2) #You can write this either way

print(f'{roommate1.name} pays: ', roommate1.pays(the_bill, roommate2))
print(f'{roommate2.name} pays: ', roommate2.pays(the_bill, roommate1))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(roommate1, roommate2, the_bill)
