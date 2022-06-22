import warnings
import GettingQuestions
from fpdf import FPDF

def MakePdf(sub,quesNum):
    # To disable the deprication warning of ln = True
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Extending the FPDF class
    class PDF(FPDF):
        def header(self):
            # font
            self.set_font('helvetica', 'B', 26)

            # Title
            self.cell(0,15,"Daily Practice Problem", align = 'C')

            # Line break
            self.ln(30)
        
        def footer(self):
            # font
            self.set_font('helvetica', 'I', 12)

            # Footer
            self.cell(0,20,"Made by Aditya (@uncanny_adi)",align = 'C')

    # Creating pdf object
    pdf = PDF('P','mm')                # 'P' represents potrait and 'mm' represents millimeters

    # Seting up auto page break
    pdf.set_auto_page_break(auto = True, margin = 35)

    # Creating a page
    pdf.add_page()

    # Setting font
    pdf.set_font('helvetica','',16)

    # Adding text
    n = 1
    questions = GettingQuestions.GetQuestions(sub,quesNum)

    for item in questions:
        pdf.cell(0,20,str(n)+") "+item,ln=True)
        n+=1

    # Creating the pdf
    pdf.output('DPP.pdf')