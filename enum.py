#open a file that has format Name = number (ex: Afghanistan = 93) - print out Member Name: + country 
#and Member value: + value
filename =open(r"C:\Users\Documents\Python Scripts\countryList.txt")
listDict = {}
for line in filename:
    key, value = [i.strip() for i in line.split('=', 1)]
    listDict[key] = value
print('Member name: ' + key)
print('Member value: ' + str(value))

#Now treat as an enum
from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember Name: {}'.format(Country.Albania.name))
print('\nMember Value: {}'.format(Country.Albania.value))

#print only the names in order by country value
print('ordered by value: ')
import enum
class Country(enum.IntEnum):
        Afghanistan = 93
        Albania = 355
        Algeria = 213
        Andorra = 376
        Angola = 244
        Antarctica = 672
print('\n'.join(' ' + s.name for s in sorted(Country)))
