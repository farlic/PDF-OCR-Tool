import re,pdf2image,PIL,pytesseract,time,os,math,sys
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = os.getcwd()+'//Tesseract-OCR//tesseract'



pages = pdf2image.convert_from_path('input.pdf',poppler_path=os.getcwd()+'//poppler-0.68.0//bin')

for index,page in enumerate(pages):
    start_time = time.time()

    if index > 1:
        sys.exit()


    print(f'Saving page {index}')
    page = page.save(f'image_{index}.jpg')

    print('Looking for text')
    text = pytesseract.image_to_string(f'image_{index}.jpg')
    with open(f'output_{index}.txt','w') as f:
        f.write(text)

    #lines = [line for line in text if line.strip() !='']

    end_time = time.time()
    print(f'Time elapsed: {round(end_time-start_time)}s')

