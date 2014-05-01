"""
Exam P Mobile Flashcards Randomization Program

"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

sys.setrecursionlimit(2000)

inputpdf = PdfFileReader(open("C:/Users/Rochester/Desktop/ExamPFlashcards.pdf", "rb"))

for i in range(0,inputpdf.numPages,2):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    output.addPage(inputpdf.getPage(i + 1))
    m = i / 2
    outputStream = open("C:/Users/Rochester/Documents/ExamP/page%s.pdf" % m, "wb")
    output.write(outputStream)
    outputStream.close()
