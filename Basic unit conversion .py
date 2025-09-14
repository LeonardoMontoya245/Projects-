# Leonardo Montoya
# lab section 02
# nov 2023
# Lab 13

# let the user to convert ounces to grams, inches to centimeters, and kilometers to miles.

 # first define/ user greeting 
def userGreeting():
    print('This program will convert Inches/Centimeters, Ounces/Grams')
    print('and Kilometers/Miles either way depending on which is centered first.')
    print()
    print('Enter I or C to convert from Inches or Centimeters.')
    print('Enter O or G to convert from Ounces or Grams.')
    print('Enter M or K to convert from MIles or Kilometers.')
    print()
# second define/ user input line 
def getConvertion():
    convert = input('Enter the type of convertion you would like to do: ').upper()
    # error check 
    while convert not in ['I', 'C', 'O', 'G', 'M', 'K',]:
        convert = input('INPUT ERROR: enter I,C,O,G,M,K: ').upper()

    return convert 


# the user input a number/ measure/ convertion 
def userInput(convert):
    convert2 = float(input('Enter a measure/Weight to convert: '))

    print()
    # if / elif statments  
    if convert == 'I':
        result = convert2 * 2.54
        print(convert2, 'Inches equal to', format(result, '.2f'), 'centimeters.')
    # user input 
    elif convert == 'C':
        result = convert2 / 2.54
        print(convert2, 'cemtimeters equal to', format(result, '.2f'), 'inches.')
    # user input
    elif convert == 'O':
        result = convert2 * 28.3495231
        print(convert2, 'Ounces equal to', format(result, '.2f'), 'Grams.')
    # user input
    elif convert == 'G':
        result = convert2 / 28.3495231
        print(convert2, 'Grams equal to', format(result, '.2f'), 'Ounces.')
    # user input
    elif convert == 'M':
        result = convert2 * 1.609344
        print(convert2, 'Miles equal to', format(result, '.2f'), 'Kilometers.')
    # user input
    elif convert == 'K':
        result = convert2 / 1.609344
        print(convert2, 'Kilometers equal to', format(result, '.2f'), 'Miles.')

# run again loop 
def runAgain():
    # user convertion input 
    choice = input('Would you like to make another conversion? (y/n): ').lower() 
    # run again 
    while choice not in ['y', 'n']:
        choice = input('INPUT ERROR: another conversion? (y/n): ').lower()

    if choice == 'n':
        run = False

    else:
        run = True


    return run 

    print()
    
# exit message 
def exitMessage():
    print() 
    print('Have a nice day')



# -------------------------------------Main--------------------------------------------

# program loop 
runM = True
while runM == True:
    # first call funcation
    userGreeting()
    print() 

    # the second call 
    convertMain = getConvertion()
    print() 

    # the third call 
    userInput(convertMain)
    print() 

    # the fouth call 
    runM = runAgain()
    print()

# the fifth call 
exitMessage()
print() 






    


