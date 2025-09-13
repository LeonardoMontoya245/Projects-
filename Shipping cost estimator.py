


# This program should let the user enter any number of items into the program and then calculate and output the Subtotal

# define the usergreeting 
def userGreeting():
    print('This program lets the user products to be shipped and calculate the')
    print('subtotal, tax, shipping and handling, and the total due.')


# state Abbreviation define /
def statesInput():

    statesAbbreviation = ['AL','AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
             'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
             'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
             'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
             'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    # user input for state Abbreviation / error check 
    choice1 = input('Please enter a state Abbreviation: ').upper()

    while choice1 not in statesAbbreviation:
        choice1 = input('INPUT ERROR: Please enter a state Abbreviation: ').upper()

    return choice1 

# user input the item quantity, weight and cost of the item 
def getProductInfo():

    productInfo = []

    run = True
    while run == True:

        itemQuantity = int(input('enter the item quantity(enter 0 if done): '))

        if itemQuantity == 0:
            run = False

        else:
            itemWeight = float(input('enter the item weight: '))

            itemCost = float(input('enter the item cost: '))

            productInfo.append([itemQuantity, itemWeight, itemCost])

    return productInfo

# the calculation for the products 
def calculate(productInfo):

    boxWeight = 0
    subTotal = 0
    # for loop 
    for mainIndex in range(len(productInfo)):

        itemQuantity, itemWeight, itemCost = productInfo[mainIndex]
        boxWeight = boxWeight + (itemQuantity * itemWeight)
        subTotal = subTotal + (itemQuantity * itemCost)

        shippingHandling = boxWeight * 0.25

        if boxWeight < 10:
            handling = 1

        elif boxWeight > 100:
            handling = 5

        else:
            handling = 3

    return subTotal, shippingHandling 

# let the user to run the program again  
def runAgain():
    # user convertion input 
    choice = input('Would you like to fill another order? (y/n): ').lower() 
    # run again 
    while choice not in ['y', 'n']:
        choice = input('INPUT ERROR: Please enter (y/n): ').lower()

    if choice == 'n':
        run = False

    else:
        run = True


    return run

#---------------------------------------------Main--------------------------------------------
# first call 
userGreeting()
print()

# main program loop 
runM = True
while runM == True:
    # 
    productInfoM = getProductInfo()
    print()

    # 
    subTotalMain, shippingHandling = calculate(productInfoM)
     

    #
    choice1M = statesInput()

    if choice1M == 'CA':
        tax = subTotalMain * .08

    else:
        tax = 0.00

    totalDue = subTotalMain + shippingHandling + tax
    print() 

    print(format('subtotal:', '<25'), format(subTotalMain, '>10,.2f'))

    print(format('shipping and Handling:', '<25'), format(shippingHandling, '>10,.2f'))

    print(format('tax:', '<25'), format(tax, '>10,.2f'))

    print(format('total Due:', '<25'), format(totalDue, '>10,.2f'))

    print() 
    
    runM = runAgain()
    print() 
     


print()
print('have a nice day') 
    
    
    

    

    
    

    

    

    
    

            
        
        
    
    

    
    


    


    
        
    
        





