import re,pdf2image,PIL,pytesseract,time,os,math,sys,regex,re
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = os.getcwd()+'//Tesseract-OCR//tesseract'



pages = pdf2image.convert_from_path('input.pdf',poppler_path=os.getcwd()+'//poppler-0.68.0//bin')
#grab page objects

for index,page in enumerate(pages):
    start_time = time.time()

    if index > 1:
        sys.exit() #temp stop for >1 page

    print(f'----------------------\nImage {index}')
    print('Looking for text')


    text = pytesseract.image_to_string(page)
    #grab text
    
    #with open(f'output_{index}.txt','w') as f:
    #    f.write(text)

    text = text.split('\n')
    text = [line for line in text if line.strip() !='']
    #split into lines, strip empty lines

    for key,line in enumerate(text): #temp output to see lines
        print(line)

    


    end_time = time.time()
    print(f'Time elapsed: {round(end_time-start_time)}s')

