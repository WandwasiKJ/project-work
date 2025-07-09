#Enter Account no.
def sendmoney():
    acct_no = input("Enter ZOLATEL account number:")
    if len(acct_no)==12 and acct_no.isnumeric():
        checkAmount(acct_no)
    else:
        print("Invalid ZOLATEL account number!\n"
              "Try again!\n"
              )

# Enter Amount
def checkAmount(x):
    amt=input("Enter Amount:")
    if amt.isnumeric():
        print(f"The {x} has been credited with UGX {amt}")
    else:
        print(
            "Invalid Amount Entry\n"
            "Try Again"
        )
        checkAmount(x)



#Airtime Transaction
def airtimeTrans():
    phone = input('Enter phone number:')
    if len(phone)== 10 and phone.isnumeric():
       checkAmount(phone)
    else:
        print(
            "Invalid phone number\n"
            "try again!\n"
        )
        airtimeTrans()

# transaction entry
def transEntry():
    transCode = input(
        "1.Check balance\n"
        "2.Buy Airtime\n"
        "3.Send Money\n"
        "select transaction:"
    )
    if transCode=="1":
       print("Your account balance is Ugx 2000")
    elif transCode=="2":
        airtimeTrans()
    elif transCode=="3":
        sendmoney()
    else:
        print("invalid entry\n"
              "try again! "
              )
        transEntry()

       
# function to crosscheck USSD code for ZOLATEL SERVICES
def confirmUSSD():
    ussd = input("Enter USSD code:")
    if ussd == "*185#":
        transEntry()
    else:
        print("invalid USSD code\n"
            "try again")
        confirmUSSD()

#Calling the function
confirmUSSD()