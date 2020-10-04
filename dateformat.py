#format date words to date


months={
'january':'01',
'february':'02',
'march':'03',
'april':'04',
'may':'05',
'june':'06',
'july':'07',
'august':'08',
'september':'09',
'october':'10',
'november':'11',
'december':'12'
}

days = {
    'first':'01',
    'second':'02',
    'third':'03',
    'fourth':'04',
    'fifth':'05',
    'sixth':'06',
    'seventh':'07',
    'eighth':'08',
    'ninth':'09',
    'tenth':'10',
    'eleventh':'11',
    'twelfth':'12',
    'thirteenth':'13',
    'fourteenth':'14',
    'fifteenth':'15',
    'sixteenth':'16',
    'seventeenth':'17',
    'eighteenth':'18',
    'nineteenth':'19',
    'twentieth':'20',
    'twenty-first':'21',
    'twenty-second':'22',
    'twenty-third':'23',
    'twenty-fourth':'24',
    'twenty-fifth':'25',
    'twenty-sixth':'26',
    'twenty-seventh':'27',
    'twenty-eighth':'28',
    'twenty-ninth':'29',
    'thirtieth':'30',
    'thirty-first':'31'
}

print('hint, Fifteenth July 2014')
date = input('input date... ')

day = ''
month = ''
year = ''

for word in date.split():
    word = word.lower()
    if word in months:
        month = months[word]
    elif word in days:
        day = days[word]
    else:
        year = word

date = f'{day}/{month}/{year}'
print(date)