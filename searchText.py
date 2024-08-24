# Warning
# Intended for educational purposes only
import re
#----------------------------------------Globals
FullText = [ ]
CollectionPhone = [ ]
CollectionEmail = [ ]
CollectionSocial = [ ]
def main():
        openText()
        checkEmail(FullText)
        checkPhone(FullText)
        checkSocial(FullText)
        displayResult()
#---------------------------------------Functions
def openText():
    #Change and comfirm file location 
    file = open("/User/"USER"/Desktop/searchText.txt", "r") 
    text = file.readlines()
    for line in text:
        FullText.append(line)
    file.close()
def checkEmail(chunk):
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # @ symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
    )''', re.VERBOSE)
    for groups in emailRegex.findall(str(chunk)):
       CollectionEmail.append(groups[0])
def checkPhone(chunk):
    phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)
    for groups in phoneRegex.findall(str(chunk)):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])   
        if groups[8] != '': 
            phoneNum += ' x' + groups[8]
        CollectionPhone.append(phoneNum)
def checkSocial(chunk):
    socialRegex = re.compile(r'''(
    (\d{3})                       # first three digits 
    (-)                           # separator
    (\d{2})                       # second two digits
    (-)                           # separator
    (\d{4})                       # third four digits
    )''', re.VERBOSE)
    for groups in socialRegex.findall(str(chunk)):
        CollectionSocial.append(groups[0])
def displayResult():
    leftWidth = 12
    rightWidth = 5
    print('\n' + ('-' * 45))
    if len(CollectionEmail) > 0:
        print('Emails found:'.center(60))
        print(('-' * 30).center(60))
        for i in CollectionEmail:
            print(i.center(60))
    else:
        print('No emails found'.center(60))
    print(('-' * 30).center(60))
    if len(CollectionPhone) > 0: 
        print('Phone numbers found:'.center(60))
        print(('-' * 30).center(60))
        for i in CollectionPhone:
            print(i.center(60))
    else:
        print('No phone numbers found'.center(60))
    print(('-' * 30).center(60))
    if len(CollectionSocial) > 0: 
        print('Social-security numbers found:'.center(60))
        print(('-' * 30).center(60))
        for i in CollectionSocial:
            print(i.center(60))
    else:
        print('No social-security numbers found'.center(60))
    print('-' * 45 + '\n')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
