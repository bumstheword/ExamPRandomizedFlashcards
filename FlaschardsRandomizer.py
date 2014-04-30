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

#inputpdf = PdfFileReader(open("C:/Users/Rochester/Desktop/ExamPFlashcards.pdf", "rb"))

for i in range(200):
    #choose a random number between 0 and length of STARTPAGE, which corresponds to section
    section = random.sample(range(len(STARTPAGE)),1)[0]
    #calculate length of section
    section_length = (ENDPAGE[section] - STARTPAGE[section] + 1)
    cards = random.sample(list(range(STARTPAGE[section], ENDPAGE[section] + 1, 2)), random.sample(list(range(1, int(section_length/2) + 1)),1)[0])
    print(section)
    print(STARTPAGE[section], ENDPAGE[section], section_length)
    print(cards)
