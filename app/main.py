from num2words import num2words
import random
import click
import numpy as np
accNo = ['0000'] # is account number
mobNum = ['9876543210'] # mobile number
accName = ['user1'] # account name
accPin = ['1234'] # accpin
accCash = [50000]
menu = '\t1. Withdraw\n\t2. Deposit\n\t3. Check Balance\n\t4. Change Pin\n\t5. Delete Account\n\t6. Logout\n\nEnter Number [1 - 5]then ENTER : '
def cashWithdraw(cash):
    myList = [2000,500,200,100] 
    myArray = np.array(myList)
    pos = (np.abs(myArray-cash)).argmin()
    remCost = cash % min(myList)
    cash -= remCost
    nearValue = myArray[pos]
    while cash >= 0:
        while (cash >= nearValue)and (cash != 0):
            print(nearValue)
            cash -=nearValue
        if (nearValue >= myList[-1])and (cash != 0):
                nearValue = myList[myList.index(nearValue)+1]
        else:
            break
    if remCost != 0:
        print(remCost)
def raNum(numLen):
    numLen = numLen -1
    raNum = str(random.randint(0,9))
    length = len(raNum)
    while length <= numLen:
        raNum = raNum+str(random.randint(0,9))
        length = length + 1
    return raNum
# print((num2words(1234, lang ='en'))) #num2words
# print(random.randint(0,9)) #random
print('\t\t\t\tWelcome - Bank of Ashif')
#while loop starts
while True:
    inAccNo = input('Enter account Number: ')
    while not inAccNo:
        inAccNo = input('Enter account Number: ')
    click.clear()
    inAccPin = input('Enter your Pin: ')
    click.clear()
    InAttempt = 4
    while not inAccPin and InAttempt>=0:
        print('\n\tYOU SHOULD WANT TO ENTER THIS\nyou have only',InAttempt,'Attempt')
        inAccPin = input('Enter your Pin: ')
        click.clear()
        InAttempt -= 1
        if InAttempt < 0:
            click.clear()
            input('Your Exited your attempt, please try again later')
    if inAccPin == '':
        continue
    if (inAccNo in accNo)and (inAccPin == accPin[accNo.index(inAccNo)]):                                                        #checking account number
        accNameDisplay = accName[accNo.index(inAccNo)]
        print('Welcome, '+accNameDisplay)
        inMenu = input(menu)
        click.clear()
        InAttempt = 4
        while not inMenu and InAttempt >= 0:
            click.clear()
            print('\n\tYOU SHOULD WANT TO ENTER THIS\nyou have only',InAttempt+1,'Attempt')
            print('Welcome, '+accNameDisplay)
            inMenu = input(menu)
            InAttempt -= 1
            if InAttempt <  0:
                click.clear()
                input('Your Exited your attempt, please try again later\npress ENTER')
        if inMenu == '1':
# --------------------------------------------------------------------
#                                                                    |
#                               menu 1                               |
#                                                                    |
# --------------------------------------------------------------------
            InAttempt = 4
            inAccCash = input('Enter Amount: ')
            while not inAccCash and InAttempt >= 0:
                inAccCash = input('Enter Amount: ')
                InAttempt -=1
                if InAttempt <  0:
                    click.clear()
                    input('Your Exited your attempt, please try again later\npress ENTER')
            if inAccCash == '':continue
            if InAttempt < 0:print('Exited maximum rount sorry, Have a Nice day')
            if inAccCash.isnumeric():
                inAccCash = int(inAccCash)
                if (inAccCash <= accCash[accNo.index(inAccNo)])and (inAccCash >=0):
                    accCash[accNo.index(inAccNo)] = accCash[accNo.index(inAccNo)] - inAccCash
                    cashWithdraw(inAccCash)
                    input('Please take your cash')
                elif inAccCash > accCash[accNo.index(inAccNo)]:
                    input('Insufficient Funds')
                inBalConfrorm = input('Can i check balance? [Y / N]: ').lower()
                if inBalConfrorm == 'y':
                    input('Your current balance is {} ,{}'.format((accCash[accNo.index(inAccNo)]),(num2words((accCash[accNo.index(inAccNo)]), lang ='en'))))
            else:input('You Entered Not a valid Number')
            
            click.clear()
            # while incash is not numeric:
            #     incash = input('Enter Amount: ')
        elif inMenu == '2':
# --------------------------------------------------------------------
#                                                                    |
#                               menu 2                               |
#                                                                    |
# --------------------------------------------------------------------
            InAttempt = 4
            inAccCash = input('Enter Amount: ')
            inAccNoOther = input('Enter Account number (if same acc no then press ENTER)')
            if inAccNoOther == '':
                if inAccCash.isnumeric():
                    inAccCash = int(inAccCash)
                    accCash[accPin.index(inAccPin)] += inAccCash
                    input('SUCCESS ! ')
                    inAccCash = str(inAccCash)
                else:
                    input('Enter value is not valid')
                inBalConfrorm = input('Can i check balance? [Y / N]: ').lower()
                if inBalConfrorm == 'y':
                    input('Your current balance is {} ,{}'.format((accCash[accPin.index(inAccPin)]),(num2words((accCash[accPin.index(inAccPin)]), lang ='en'))))
            elif inAccNoOther.isnumeric():
                if inAccNoOther in accNo:
                    print('Deposit to',accName[accNo.index(inAccNoOther)])
                    if inAccCash.isnumeric():
                        inAccCash = int(inAccCash)
                        accCash[accPin.index(inAccPin)] -= inAccCash
                        accCash[accNo.index(inAccNoOther)] += inAccCash
                        print('SUCCESS ! ')
                        inBalConfrorm = input('Can i check balance? [Y / N]: ').lower()
                        if inBalConfrorm == 'y':
                            input('Your current balance is {} ,{}'.format((accCash[accNo.index(inAccNo)]),(num2words((accCash[accNo.index(inAccNo)]), lang ='en'))))
                    else:input('you Enters is not valid')
                else:input('You entered Account number not Valid')                
            else:
                input('somthing Went Wrong, Please contact Admin')
                        
            click.clear()
        elif inMenu == '3':
# --------------------------------------------------------------------
#                                                                    |
#                               menu 3                               |
#                                                                    |
# --------------------------------------------------------------------
            input('Your current balance is {} ,{}\npress ENTER to exit. '.format((accCash[accNo.index(inAccNo)]),(num2words((accCash[accNo.index(inAccNo)]), lang ='en'))))
            click.clear()
        elif inMenu == '4':
# --------------------------------------------------------------------
#                                                                    |
#                               menu 4                               |
#                                                                    |
# --------------------------------------------------------------------
            oldInAccPin=input('Enter your old pin: ')
            InAttempt = 4
            while ((not oldInAccPin)and (InAttempt>=0)):
                print('you have only',InAttempt+1,'Attempt')
                oldInAccPin=input('Enter your old pin: ')
                InAttempt -= 1
                if InAttempt <= 0:
                    input('Your Exited your attempt, please try again later')
            click.clear()
            newInaccpin = input('Enter your NEW pin: ')
            InAttempt = 4
            while ((not newInaccpin)and (InAttempt>=0)):
                print('you have only',InAttempt+1,'Attempt')
                newInaccpin=input('Enter your old pin: ')
                InAttempt -= 1
                if newInaccpin == accPin[accPin.index(inAccPin)]:
                    input('Try again, old pin and new are same ')
                    InAttempt += 1
                if InAttempt <= 0:
                    input('Your Exited your attempt, please try again later')
            if (newInaccpin != '')and (oldInAccPin != ''):
                accPin[accPin.index(inAccPin)] = newInaccpin
                input('SUCCESS !')
                click.clear()
        elif inMenu == '5':
# --------------------------------------------------------------------
#                                                                    |
#                               menu 5                               |
#                                                                    |
# --------------------------------------------------------------------
            inAccPin = input('Enter your pin: ')
            InAttempt = 4
            while ((not inAccPin)and InAttempt>=0):
                print('\tyou have only',InAttempt+1,'Attempt')
                inAccPin = input('Enter your pin: ')
                InAttempt -=1
                if InAttempt<=0:
                    input('Your Exited your attempt, please try again later')
            if inAccPin == accPin[accNo.index(inAccNo)]:
                inMobNum = input('Enter your mobilenumber: ')
                InAttempt = 4
                while ((not inMobNum)and InAttempt>=0):
                    print('\tyou have only',InAttempt+1,'Attempt')
                    inMobNum = input('Enter your mobile number: ')
                    InAttempt -=1
                    if InAttempt<=0:
                        input('Your Exited your attempt, please try again later')
                if (inMobNum !='')and (inAccPin != '') and (inMobNum == mobNum[accNo.index(inAccNo)]):
                    input('We send otp to your mobile number\n[press ENTER for it]')
                    mobOtp=raNum(4)
                    print('your OTP is',mobOtp)
                    inmobOPT = input('Enter OTP : ')
                    InAttempt = 4
                    while ((not inmobOPT)and InAttempt>=0):
                        print('\tyou have only',InAttempt+1,'Attempt')
                        inmobOPT = input('Enter your mobile number: ')
                        InAttempt -=1
                        if InAttempt<=0:
                            input('Your Exited your attempt, please try again later')
                    inaccno1 = accNo.index(inAccNo)
                    if inmobOPT == mobOtp:
                        accNo.pop(inaccno1)
                        mobNum.pop(inaccno1)
                        accName.pop(inaccno1)
                        accPin.pop(inaccno1)
                        accCash.pop(inaccno1)
                        input('SUCESS !, Good bye. ')   
                else:input('wrong mobile number')
            else:input('wrong accont pin \n[ENTER] ')
            click.clear()
        elif inMenu == '':
            continue
    else:  #inAccNo not in accNo:
        createAcc = input('\tACCOUNT NUMBER DOES NOT EXIST\n\tpress [Y] and create account else ENTER:  ').lower()
        InAttempt = 4
        while (((not createAcc) and InAttempt>=0)):
            print('\n\tYOU SHOULD WANT TO ENTER THIS\nyou have only',InAttempt+1,'Attempt')
            createAcc = input('\tACCOUNT NUMBER DOES NOT EXIST\n\tpress [Y] and create account else ENTER:  ').lower()
            InAttempt -= 1
            if InAttempt <= 0:
                input('Your Exited your attempt, please try again later')
        click.clear()
        if createAcc == 'y':            # process for creating account
            inAccNo = raNum(5)
            while inAccNo in accNo:
                 inAccNo = raNum(5)
            inAccPin = raNum(4)
            inAccName = input('Enter your Offcial Name: ')
            inMobNum = input('Enter your mobile number: ')
            while (((not inAccName) or (not inMobNum))and InAttempt>=0):
                print('\n\tYOU SHOULD WANT TO ENTER THIS\nyou have only',InAttempt+1,'Attempt')
                if inAccName == '':
                    inAccName = input('Enter your Offcial Name: ')
                if inMobNum == '':
                    inMobNum = input('Enter your mobile number: ')
                InAttempt -= 1
                if InAttempt <= 0:
                    click.clear()
                    input('Your Exited your attempt, please try again later')
            accNo.append(inAccNo)
            accName.append(inAccName)
            mobNum.append(inMobNum)
            accPin.append(inAccPin)
            print('\tYour Account number is',inAccNo,'\n\tYour Account Name is',inAccName,'\n\tYour MObile number is',inMobNum,'\n\tYour atm pin is Sended to Mobile number Please change after login, Happy Banking')
            input('press ENTER for OTP: ')
            input('Your Pin is \''+inAccPin+'\'')
            click.clear()
        else:
            click.clear()