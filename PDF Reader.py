import pyttsx3
import PyPDF2
book = open('IELTS.pdf', 'rb')
pdfReared = PyPDF2.PdfFileReader(book)
pages = pdfReared.numPages
print(pages)
friend = pyttsx3.init()
for num in range(3 , pages):
    page = pdfReared.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()

