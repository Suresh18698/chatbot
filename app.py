from transformers import pipeline
from PyPDF2 import PdfReader

# creating a pdf reader object 
reader = PdfReader('example.pdf') 

# printing number of pages in pdf file 
n = len(reader.pages)
for i in range(n):
  page = reader.pages[i] 
  i=i+1
# extracting text from page 
text = page.extract_text() 


def summary(text):
    # using pipeline API for summarization task
    summarization = pipeline("summarization")
    original_text = text
    summary_text = summarization(original_text)[0]['summary_text']
    print("Summary:", summary_text)
summary(text)
