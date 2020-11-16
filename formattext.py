import os,regex,re

with open('clean please.txt','r') as f:
    text = f.readlines()
    text = [line for line in text if line.strip() !='']

for key,line in enumerate(text):
    line = str(line).lower()

person = {
    'district':'',
    'dod':'',
    'name':'',
    'maiden':'',
    'dob':'',
    'pob':'',
    'address':'',
    'informant_name':'',
    'informant_address':'',
    'reg':''
}
# loop finder through for text,dict key, optional +- line reqs


def districtfind(text):
    for key,line in enumerate(text):
        #print(f'looking for district in line {key}')
        if regex.search('(registration){e<=2}',line):
            person['district'] = text[key].strip()
            return

def dodfind(text):
    for key,line in enumerate(text):
        if regex.search('(date and place of death){e<=3}',line):
            person['dod'] = text[key+1].strip()
            return

def namefind(text):
    for key,line in enumerate(text):
        if regex.search('(name and surname){e<=2}',line):
            person['name'] = text[key+1].strip()
            return

def maidenfind(text):
    for key,line in enumerate(text):
        if regex.search('(married){e<=2}',line):
            person['maiden'] = text[key+1].strip()
            return

def dobfind(text):
    for key,line in enumerate(text):
        if regex.search('(date and place of birth){e<=3}',line):
            person['dob'] = text[key+1].strip()
            return

def pobfind(text):
    for key,line in enumerate(text):
        if regex.search('(date and place of birth){e<=3}',line):
            person['pob'] = text[key+2].strip()
            return

def address(text):
    for key,line in enumerate(text):
        if regex.search('(usual address){e<=3}',line):
            person['address'] = text[key+2].strip()
            return

def informant_name(text):
    for key,line in enumerate(text):
        if regex.search('(informant){e<=3}',line):
            person['informant_name'] = text[key+1].strip()
            return

def informant_address(text):
    for key,line in enumerate(text[20:]):
        if regex.search('(usual address){e<=3}',line):
            person['informant_address'] = text[20+key+1].strip()
            return

def reg(text):
    for key,line in enumerate(text):
        if regex.search('(date of registration){e<=3}',line):
            person['reg'] = text[key+1].strip()
            return

districtfind(text)
dodfind(text)
namefind(text)
maidenfind(text)
dobfind(text)
pobfind(text)
address(text)
informant_name(text)
informant_address(text)
reg(text)

gender_pattern = re.compile("( (fe)?male)",re.I) #compile makes and pattern object that re.I ignores case.
person['name'] = gender_pattern.sub("",person['name'])
# .sub is just a method, silly.      'replace this'.sub('with this','in this')

relative_pattern = re.compile("( (bro|mo|fa)?ther|sister|informant|causing the body to be cremated|uncle)",re.I)
person['informant_name'] = relative_pattern.sub("",person['informant_name'])

person['reg'] = person['reg'][:re.search(r'\d+',person['reg']).span()[1]]

remove_districts = []
district_pattern = regex.compile('(registration district|Administrative area){e<=1}',re.I)
iterator = district_pattern.finditer(person['district'])
for match in iterator:
    #print(match.span())
    remove_districts.append(match.span())
person['district'] = person['district'][remove_districts[0][1]:remove_districts[1][0]].strip()

for pair in person.items():
    print(pair) 

exit = input()