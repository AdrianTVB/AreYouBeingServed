import os.path
import string
#import nltk

#nltk.download('punkt')

# Functions to process minutes


def subString(text="", startWord=None, endWord=None):
    # Function to return the substring between the first occurrences of 2 words
    # Check text was provided
    if len(text) <= 0:
        print("Valid text must be provided.")
        return ""
    # Convert text to lowercase
    lText = text.lower()
    #Identify the start and stop positions for the subset (handling missing arguments)
    if startWord:
        startPos = lText.find(startWord)
    else:
        print("Start word not provided.  Started from beginning of the string.")
        startPos = 0

    if endWord:
        endPos = lText.find(endWord)
    else:
        print("End word not provided.  Ended at the end of the string.")
        endPos = len(text)
    # Return the subString
    return (text[startPos:endPos])


def attendList(minuteAttend, names):
    # Function to return a list of attendees, given some text and a list of surnames.

    # Remove punctuation
    cleanText = minuteAttend.translate(str.maketrans('', '', string.punctuation))
    # Convert text into a set
    minSet = set(cleanText.split())

    # Convert names into a set
    nameSet = set(names)

    # Return the intersection of the sets as a list
    return(list(nameSet.intersection(minSet)))

#variables
#startWord = "present:"
#endWord = "attendance:"
#surnameList = ["Hazlehurst", "Barber", "Dixon", "Harvey", "Heaps", "Kerr", "Lawson", "Lyons", "Nixon", "O’Keefe", "Poulain", "Redstone", "Schollum", "Travers", "Watkins"]

# Read in get_text
#fileDir = "scrape/data/txt/"
#fileName = "20190822_hdc_Council.txt"

#with open(os.path.join(fileDir, fileName), "r") as f:
#    rawText = f.read()


#attendText = subString(text=rawText, startWord=startWord, endWord=endWord)


#attendance = attendList(attendText, surnameList))






#print(text)
# extract attendance get_text
#tokens = nltk.word_tokenize(rawText)
#text = nltk.Text(tokens)

#print("nltk")
#text.concordance('attendance')
#print(text.index('present'))
#print(text.index('attendance'))


# create attendance list
