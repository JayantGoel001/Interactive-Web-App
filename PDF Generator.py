from pywebio import *
from fpdf import FPDF


def createPDF(filename, pages, font, size):
    pdf = FPDF()

    pdf.set_font(font, '', size)

    if filename.split(".")[-1] != "pdf":
        filename += ".pdf"

    for text in pages:
        pdf.add_page()
        lines = text.split("\n")
        for i in range(len(lines)):
            pdf.cell(40, 10, lines[i], 0, i + 1)

    pdf.output(filename, 'F')


def app():
    filename = input.input(placeholder="Name of your file?", required=True)
    fonts = ['Helvetica', 'Calibri', 'Futura', 'Garamond', 'Times New Roman', 'Arial', 'Cambria', 'Verdana', 'Rockwell']
    text_info = input.input_group("Text Font And Size", [
        input.select('Select your font', options=fonts, value='Arial', name='Font'),
        input.input('Select your text size', value='16', type=input.NUMBER, name='Size')
    ])
    add_more = True
    pages = []
    while add_more:
        page = input.textarea(placeholder="Type Here......", required=True)
        pages.append(page)
        add_more = input.actions("Would You like to add another page?", buttons=[
            {'label': 'yes', 'value': True},
            {'label': 'no', 'value': False}
        ])

    createPDF(filename, pages, text_info['Font'], text_info['Size'])
    output.put_text("PDF created.")


if __name__ == '__main__':
    start_server(app, port=8080, debug=True)
