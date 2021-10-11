# Roommates
Title: Roommates Bill
Description: An app that gets as input the amount of a bill for a particular period
and the # days that each of the roommate stayed in the house for that period
and returns how much each roommate has to pay. It also generates a PDF report
stating the names of the roommate, the period, and how much each of them had to pay.

Program "layout"

Objects: Bill:
            amount
            period
         Roommate:
            name
            days_in_house
            pays(bill)
         PdfReport:
            filename
            generate(roommate1, roommate2, bill)