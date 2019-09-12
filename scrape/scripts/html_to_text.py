# Initial script sourced from https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

#import urllib
import requests
from bs4 import BeautifulSoup
import os.path

## TODO Turn into a function so given a url and filename and directory it will parse the url and put into the file.

# Url from browser is to the navigation frame, drop the _WEB to get to the contents
#url = "http://hastings.infocouncil.biz/Open/2019/08/COR_22082019_MIN_4613_WEB.htm"
url = "http://hastings.infocouncil.biz/Open/2019/08/COR_22082019_MIN_4613.htm"

# save as text file
fileDate = "20190822"
meetingType = "Council"
organisation = "hdc"
outputDir = "data/txt/"
outputFile = fileDate + "_" + organisation + "_" + meetingType + ".txt"


# Old code from original post (uses urllib)
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html)

def html_to_txt(url, outputDir, outputFile):
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



    with open(os.path.join(outputDir, outputFile), "w") as f:
        f.write(text)


html_to_txt(url=url, outputDir=outputDir, outputFile=outputFile)
