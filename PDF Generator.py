from pywebio import *
from fpdf import FPDF


def createPDF(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 16)

    lines = text.split("\n")
    for i in range(len(lines)):
        pdf.cell(40, 10, lines[i], 0, i + 1)

    if filename.split(".")[-1]!="pdf":
        filename+=".pdf"
    pdf.output(filename, 'F')

def app():
    filename = input.input(placeholder="Name of your file?", required=True)
    text = input.textarea(placeholder="Type Here......", required=True)
    createPDF(filename, text)
    output.put_text("PDF created.")


if __name__ == '__main__':
    start_server(app, port=8080, debug=True)
