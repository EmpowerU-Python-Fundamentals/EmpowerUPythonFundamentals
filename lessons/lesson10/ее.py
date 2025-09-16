import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path("ee.pdf")
text = ""
for page in pages:
    text += pytesseract.image_to_string(page, lang="ukr+rus")
print(text)