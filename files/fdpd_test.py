from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Add some text to the
pdf.set_font(family='Times', size=24, style='B')