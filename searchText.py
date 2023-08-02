import re
#----------------------------------------Globals
fullText = [ ]
collectionPhone = [ ]
collectionEmail = [ ]
collectionSocial = [ ]
def main():
        openText()
        checkEmail(fullText)
        checkPhone(fullText)
        checkSocial(fullText)
        displayResult()
#---------------------------------------Functions
def openText():
    # Create a searchText.txt file containing text to search 
    file = open("/User/"USER"/Desktop/searchText.txt", "r") 
    text = file.readlines()
    for line in text:
        fullText.append(line)
    file.close()
def checkEmail(chunk):
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # @ symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
    )''', re.VERBOSE)
    for groups in emailRegex.findall(str(chunk)):
       collectionEmail.append(groups[0])
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
        collectionPhone.append(phoneNum)
def checkSocial(chunk):
    socialRegex = re.compile(r'''(
    (\d{3})                       # first three digits 
    (-)                           # separator
    (\d{2})                       # second two digits
    (-)                           # separator
    (\d{4})                       # third four digits
    )''', re.VERBOSE)
    for groups in socialRegex.findall(str(chunk)):
        collectionSocial.append(groups[0])
def displayResult():
    leftWidth = 12
    rightWidth = 5
    print('\n' + ('-' * 45))
    if len(collectionEmail) > 0:
        print('Emails found:'.center(60))
        print(('-' * 30).center(60))
        for i in collectionEmail:
            print(i.center(60))
    else:
        print('No emails found'.center(60))
    print(('-' * 30).center(60))
    if len(collectionPhone) > 0: 
        print('Phone numbers found:'.center(60))
        print(('-' * 30).center(60))
        for i in collectionPhone:
            print(i.center(60))
    else:
        print('No phone numbers found'.center(60))
    print(('-' * 30).center(60))
    if len(collectionSocial) > 0: 
        print('Social-security numbers found:'.center(60))
        print(('-' * 30).center(60))
        for i in collectionSocial:
            print(i.center(60))
    else:
        print('No social-security numbers found'.center(60))
    print('-' * 45 + '\n')

main()
