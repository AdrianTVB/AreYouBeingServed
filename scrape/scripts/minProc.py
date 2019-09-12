import os.path
import nltk

nltk.download('punkt')

# Functions to process minutes

# Read in get_text
fileDir = "data/txt/"
fileName = "20190822_hdc_Council.txt"

with open(os.path.join(fileDir, fileName), "r") as f:
    rawText = f.read()

#print(text)
# extract attendance get_text
tokens = nltk.word_tokenize(rawText)
text = nltk.Text(tokens)

text.concordance('attendance')
print(text.index('present'))
print(text.index('attendance'))


# create attendance list
