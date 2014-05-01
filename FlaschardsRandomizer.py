"""
Coaching Actuaries
Exam P Mobile Flashcards Randomized Program

Michael Goulet
Profile Insurance Group
goulet.michaelrobert@gmail.com
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import random

sys.setrecursionlimit(2000)
STARTPAGE = [3,37,47,49,63,91,119,131,151,153,157,191,213,225,247,267,289,311,321,327,349,367,399,417]
ENDPAGE = [36,46,48,60,90,118,130,150,152,156,190,212,222,246,266,288,310,320,326,348,364,398,416,422]

# Choose desired sections. Then card order is randomized with question card followed by answer card.
def ChooseCards(sections = [0]):
    section_lengths = []
    card_pool = []
    final = []

    # Creates card pool from the passed sections array.
    for i in sections:
        # section_lengths += [ENDPAGE[sections[i]] - STARTPAGE[sections[i]] + 1]
        card_pool += list(range(STARTPAGE[i], ENDPAGE[i] + 1))

    # Samples from only the odd cards in the card pool and stores results of the sample.
    cards = random.sample(card_pool[0:len(card_pool):2], int(len(card_pool)/2))

    # Combines the odd cards with corresponding even cards
    for i in cards:
        final += [i]
        final += [i + 1]
    return(final)



# Read in the ordered card PDF
inputpdf = PdfFileReader(open("/Users/michaelgoulet/Desktop/ExamPFlashcards.pdf", "rb"))
output = PdfFileWriter()
cards = ChooseCards()
# Build the randomized card PDF
for i in cards:
    output.addPage(inputpdf.getPage(i - 1))
#Create and write the file
outputStream = open("/Users/michaelgoulet/Desktop/TESTING.pdf", "wb")
output.write(outputStream)
outputStream.close()
