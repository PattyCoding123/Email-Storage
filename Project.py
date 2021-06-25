#Patrick Ducusin

nameAndEmailDct = {} #initializing the dictionary

def infoMenu(): #This will be the menu displayed to the user so they know what choices they can make
    print('Menu')
    print('-----------------------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the Program')

def lookUpInfo(): #This will be the function for option 1 in the menu
    inputName = input('Enter a name: ')
    inputName = inputName.upper()
    if inputName in nameAndEmailDct:
        print('Email:', nameAndEmailDct[inputName])

    else:
        print('Sorry, but the name entered was not found')

def addInfo(): #This will be the function for option 2
    inputName = input('Enter the name you wish to add: ')
    inputName = inputName.upper()
    if inputName not in nameAndEmailDct:
        inputEmail = input('Enter the correct email address: ')
        nameAndEmailDct[inputName] = inputEmail
        print('Name and email have successfully been added')

    else:
        print('This person already exists in the dictionary')

def changeInfo(): #This will be function for option 3
    inputName = input('Enter the name of the person whose email address you want to change: ')
    inputName = inputName.upper()
    if inputName in nameAndEmailDct:
        newEmail = input('Enter the new email: ')
        nameAndEmailDct[inputName] = newEmail

    else:
        print('Sorry, but the name entered was not found')


def deleteInfo(): #This will be the function for option 4
    inputName = input('Enter name of the person whose information you wish to delete: ')
    inputName = inputName.upper()
    if inputName in nameAndEmailDct:
        flag = True
        while flag == True: #Asks the user again if they really want to delete the file
            askAgain = input('Are you sure?(Enter y for yes, n for no): ')
            if askAgain == 'y':
                del nameAndEmailDct[inputName]
                print('Information successfully deleted')
                flag = False

            elif askAgain == 'n':
                print("Ok, the person's information will not be deleted")
                flag = False

            else: 
                print('Not a valid input')
                flag = True

    else:
        print('Sorry, but the name entered was not found')




flag01 = True
while flag01 == True: #Asks the user if it's their first time using the program. If it is, then it goes straight into the menu
    returningUser = input('Is this your first time using this program?(Enter y for yes, n for no): ')
    if returningUser == 'n': #If the user has already used the program before, it will read the saved names and email addresses and store them into a dictionary
        dataFile = open('emailInfo.txt','r')
        for aline in dataFile:
            aline = aline.strip()
            aline = aline.split()
            nameAndEmailDct[aline[0]] = aline[1]
        dataFile.close()
        flag01 = False
    elif returningUser == 'y':
        print('Welcome to the Program!')
        flag01 = False
    else: #If the user doesn't input y or n, it will ask them to try again
        print('Not a valid input, try again')
        flag01 = True

flag02 = True 
while flag02 == True:
    print()
    infoMenu() #This will show the user the menu options 
    userInput = input('Please enter a choice (1 through 5): ') #detects the user's input and calls the functions corresponding to the number they enter
    if userInput == '1':
        lookUpInfo()
        flag02 = True
    elif userInput == '2':
        addInfo()
        flag02 = True
    elif userInput == '3':
        changeInfo()
        flag02 = True
    elif userInput == '4':
        deleteInfo()
        flag02 = True
    elif userInput == '5':
        savedData = open('emailInfo.txt','w')
        for name in nameAndEmailDct: #This will store the names and emails in the dictionary into a file
            savedData.write(name + ' ' + nameAndEmailDct[name] + '\n')
        savedData.close()
        flag02 = False
    else: #If the user enters something invalid, the program will ask the user to try again
        print('Please enter a valid input')
        flag02 = True

print('Information has been successfully saved')
print('Goodbye!')
   



    

        
        
        
        
    
    
