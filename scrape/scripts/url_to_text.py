# Initial script sourced from https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

#import urllib
import requests
from bs4 import BeautifulSoup


#from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from urllib.request import urlopen
#from StringIO import StringIO
from io import StringIO, BytesIO
#import os
import sys, getopt

## TODO Turn into a function so given a url and filename and directory it will parse the url and put into the file.

# Url from browser is to the navigation frame, drop the _WEB to get to the contents
#url = "http://hastings.infocouncil.biz/Open/2019/08/COR_22082019_MIN_4613_WEB.htm"
#url = "http://hastings.infocouncil.biz/Open/2019/08/COR_22082019_MIN_4613.htm"

# save as text file
#fileDate = "20190822"
#meetingType = "Council"
#organisation = "hdc"
#outputDir = "data/txt/"
#outputFile = fileDate + "_" + organisation + "_" + meetingType + ".txt"


# Old code from original post (uses urllib)
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html)

def html_to_txt(url):
    page_response = requests.get(url, timeout=5)

    soup = BeautifulSoup(page_response.content, "html.parser")

    # For downloaded html
    #html = open("ncc1.html").read()
    #page_content = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    #print(text)
    return text


#html_to_txt(url=url, outputDir=outputDir, outputFile=outputFile)


#converts pdf, returns its text content as a string
# modified from https://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php#4
# using https://stackoverflow.com/questions/9751197/opening-pdf-urls-with-pypdf
def pdf_to_txt(url, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    infile = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    #infile = file(fname, 'rb')
    #remote_file = urlopen(Request(url)).read()
    remote_file = urlopen(url).read()
    infile = BytesIO(remote_file)

    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
