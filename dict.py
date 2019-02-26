#open a file that has format Name = number (ex: Afghanistan = 93) - print out Member Name: + country 
#and Member value: + value
filename =open(r"C:\Users\Documents\Python Scripts\countryList.txt")
listDict = {}
for line in filename:
    key, value = [i.strip() for i in line.split('=', 1)]
    listDict[key] = value
print('Member name: ' + key)
print('Member value: ' + str(value))
