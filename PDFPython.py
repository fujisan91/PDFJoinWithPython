from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.colors import  Color

def create_pdfFile(size):
    red50transparent = Color( 0, 0, 0, alpha=1)
    pdfFile = canvas.Canvas('./python.pdf')
    pdfFile.saveState()
    
    pdfFile.setAuthor('python-izm.com')
    pdfFile.setTitle('PDF生成')
    pdfFile.setSubject('サンプル')
    # A4
    pdfFile.setPageSize((21.0*cm, 29.7*cm))

    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
    pdfFile.setFont('HeiseiKakuGo-W5', 12)
    pdfFile.setFillColor(red50transparent)
    pdfFile.drawString(5*cm, 25*cm, 'あいうえおー')
    pdfFile.restoreState()
    pdfFile.save()


def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    create_pdfFile('A4')

    create_watermark(
        input_pdf='取得支援資格手当一覧.pdf', 
        output='watermarked_notebook.pdf',
        watermark='python.pdf')