import re,pdf2image,PIL,pytesseract,time,os,math,sys,regex,re
from PIL import Image

print(r'''
 _____  _____  ______ 
|  __ \|  __ \|  ____|
| |__) | |  | | |__   
|  ___/| |  | |  __|  
| |    | |__| | |     
|_|    |_____/|_|     

  ____   _____ _____  
 / __ \ / ____|  __ \ 
| |  | | |    | |__) |
| |  | | |    |  _  / 
| |__| | |____| | \ \ 
 \____/ \_____|_|  \_\
 ''')

print('----------------------\nsetting working directory')
pytesseract.pytesseract.tesseract_cmd = os.getcwd()+'//Tesseract-OCR//tesseract'
print('pytesseract located\nloading PDF')
pages = pdf2image.convert_from_path('input.pdf',poppler_path=os.getcwd()+'//poppler-0.68.0//bin')
print('pdf loaded')
#grab page objects

class Person:
	def __init__(self):
		self.district = ''
		self.dod = ''
		self.name = ''
		self.gender = ''
		self.maiden = ''
		self.dob = ''
		self.pob = ''
		self.usual_address = ''
		self.informant_name = ''
		self.qualification = ''
		self.informant_address = ''
		self.reg_date = ''

print('----------------------\ncompiling regular expressions')
gender_pattern = re.compile("( (fe)?male)",re.I)
relative_pattern = re.compile("((bro|mo|fa)?ther|sister|informant|causing the body to be cremated|uncle)",re.I)
district_pattern = regex.compile('(?i)(registration district|Administrative area){e<=1}')

for index,page in enumerate(pages):
    start_time = time.time()

    p = Person()

    if index >= 1:
        sys.exit() #temp stop for >1 page

    print(f'----------------------\nImage {index}')
    text = pytesseract.image_to_string(page)
    #grab text
    
    #with open(f'output_{index}.txt','w') as f:
    #    f.write(text)
    text = text.split('\n')
    text = [line for line in text if line.strip() !='']
    #split into lines, strip empty lines

    for key,line in enumerate(text): #temp output to see lines
        #print(line)

        if regex.search('(?i)(registration){e<=2}',line): #(?i) is the old regex ignore case
            p.district = text[key].strip()

        elif regex.search('(?i)(date and place of death){e<=3}',line):# {e<3} is fuzzy match
            p.dod = text[key+1].strip()

        elif regex.search('(?i)(name and surname){e<=2}',line):
            p.name = text[key+1].strip()

        elif regex.search('(?i)(married){e<=2}',line): #this needs fixing
            p.maiden = text[key+1].strip()

        elif regex.search('(?i)(date and place of birth){e<=3}',line):
            p.dob = text[key+1].strip()

        elif regex.search('(?i)(date and place of birth){e<=3}',line):
            p.pob = text[key+2].strip()

        elif regex.search('(?i)(usual address){e<=3}',line):
            p.usual_address = text[key+2].strip()

        elif regex.search('(?i)(informant){e<=3}',line):
            p.informant_name = text[key+1].strip()

        elif regex.search('(?i)(usual address){e<=3}',line):
            p.informant_address = text[20+key+1].strip()

        elif regex.search('(?i)(date of registration){e<=3}',line):
            p.reg_date = text[key+1].strip()

        
    #cleaning scraped results
    p.gender = gender_pattern.search(p.name[-7:]).group(0)
    p.name = p.name[:-7]+gender_pattern.sub("",p.name[-7:])
    p.reg_date = p.reg_date[:re.search(r'\d+',p.reg_date).span()[1]]

    remove_districts = []
    district_iterator = district_pattern.finditer(p.district)
    for match in district_iterator:
        remove_districts.append(match.span())
    p.district = p.district[remove_districts[0][1]:remove_districts[1][0]].strip()

    #District
    #DoD
    #Name
    #Gender
    #Maiden Name
    #DoB
    #PoB
    #Usual Address
    #Informant Name
    #Qualification
    #Informant Address
    #Date of Registration

    for x,y in vars(p).items():
        print(f'{x} : {y}')

    end_time = time.time()
    print(f'Time elapsed: {round(end_time-start_time)}s')

