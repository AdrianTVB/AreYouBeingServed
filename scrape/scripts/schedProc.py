from bs4 import BeautifulSoup
import requests
import csv
import re


def meetInfoCouncilScrape(url = None, file = None):
    # Scrape meeting information and links to minutes from an InfoCouncil webpage
    # The webpage can be provided as either a url, or downloaded html file
    if url:
        page_response = requests.get(url, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
    elif file:
        html = open(file).read()
        page_content = BeautifulSoup(html, "html.parser")
    else:
        print("A file path or url must be provided")
        return {}
    # Select the table that has all of the meetings set out in it
    table = page_content.find(lambda tag: tag.name=='table' and tag.has_attr("id") and tag['id']=="grdMenu")
    # Create list to hold the results
    output_list = []
    # Process each row of the table
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        meeting = {}
        #output_row = []
        col = 1
        # Extract relevant data from the columns
        for column in columns:
            # clean the text
            outtxt = column.text.replace('\n', ' ')
            # create a list to hold the links
            links = []
            # Identify and clean the links
            for link in column.findAll('a'):
                minutes = {}
                # Process the text to determine the type of document, pdf or html
                rawtxt = link.text
                if rawtxt != None and rawtxt.lower().find('pdf') != -1:
                    minutes['Type'] = 'pdf'
                elif rawtxt != None and rawtxt.lower().find('html') != -1:
                    minutes['Type'] = 'html'
                elif rawtxt != None:
                    minutes['Type'] = 'missed'
                else:
                    minutes['Type'] = ''
                # Process the link so that it is usable (works for ncc Infocouncil, not tested on others)
                rawlink = link['href']
                cleanLink = rawlink[(rawlink.find('=')+1):]
                # the cleanlink needs _WEB chopped out of it in order for it to provide the useful url
                minutes['url'] = targetUrl + cleanLink.replace('_WEB', '')
                links.append(minutes)
            # create the meeting info
            if col == 1:
                meeting['Date'] = outtxt
            elif col == 2:
                meeting['Type'] = outtxt
            elif col == 5:
                meeting['url'] = links

            col += 1
        # append the meeting to the output
        output_list.append(meeting)

    return output_list


#print(meetInfoCouncilScrape(url = "http://napier.infocouncil.biz/"))
#print(meetInfoCouncilScrape(file = "scrape/data/html/ncc1.html"))
