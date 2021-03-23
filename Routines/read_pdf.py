from PyPDF2 import PdfFileReader
from datetime import datetime

# path = "/Users/mr/Documents/scrapy_tutorial/Routines/2021-02-24 (34).pdf"
def get_info(path):
    with open(path, "rb") as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_pages = pdf.getNumPages()
        date = datetime.strptime(info["/ModDate"],'%y/%m/%d %H:%M:%S')

    print (info)
    print (date)
    # print (info["/ModDate"])

    # author = info.author
    # creator = info.creator
    # producer = info.producer
    # subject = info.subject
    # title = info.title

if __name__ == '__main__':
    path = "/Users/mr/Documents/scrapy_tutorial/Routines/2021-02-24 (34).pdf"
    get_info(path)
