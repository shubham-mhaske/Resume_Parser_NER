from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO

import textract
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter  # process_pdf
from pdfminer.pdfpage import PDFPage


def read_file(filename):
    # convert pdf to text
    def pdf_to_text(filename):

        # PDFMiner boilerplate
        rsrcmgr = PDFResourceManager()
        sio = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # Extract text
        fp = open(filename, 'rb')
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
        fp.close()

        # Get text from StringIO
        text = sio.getvalue()

        # Cleanup
        device.close()
        sio.close()

        return text

        # for converting .doc, .docx to text

    def docs_to_text(filename):
        text = textract.process(filename)
        text = text.decode("utf-8")
        return text

    try:
        if (filename[filename.find('.') + 1:]) == 'pdf':
            return pdf_to_text(filename)
        elif (filename[filename.find('.') + 1:]) in ('doc', 'docx'):
            return docs_to_text(filename)
    except:
        print('Not a valid file format')
