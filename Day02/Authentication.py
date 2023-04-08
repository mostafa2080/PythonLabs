import time
import re

from MainPage import mainPage

def entryInputValidation():
    x = input("Enter Your Choice: ")
    if (x.isdigit() and int(x) in [1, 2]):
        return int(x)
    return entryInputValidation()



#name validation
def enterFName():
    x = input("Enter your First Name: ")
    if (x.isalpha() or not x):
        return x
    else:
        print("invalid name (should be alphabetic only)")
        return enterFName()


def enterSName():
    x = input("Enter your second Name: ")
    if (x.isalpha() or not x):
        return x
    else:
        print("invalid name (should be alphabetic only)")
        return enterSName()


#email
def enteremail():
    x = input("Enter email: ")
    if emailvalidator(x):
        return x
    else:
        print("Invalid Email")
        return enteremail()

#emailValidation
def emailvalidator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


#password
def enterPassword():
    x = input("Enter Password: ")
    if (len(x) < 8 or not x):
        return enterPassword()
    else:
        Confirmed_password = Confirm_password(x)
        if Confirmed_password:
            return x
        else:
            print("Weak Password ")
            return enterPassword()

#passwordConfirmation
def Confirm_password(Password):
    x = input("Enter Password Again: ")
    if (Password == x or not x):
        return True
    else:
        print("Password Not Matched")
        return False


#phone
def enterPhone():
    x = input("Enter Your Phone: ")
    if (re.match(r"^01[0-2,5]\d{1,8}$", x)):
        return x
    else:
        print('invalid phone number')
        return enterPhone()


#save data
def saveData(data):
    file = open('usersdata.txt', 'a')
    file.writelines(data)
    file.close
    print("Registered Successfully!")

#registeration
def Registration():
    FirstName = enterFName()
    secondName = enterSName()
    email = enteremail()
    Password = enterPassword()
    phone = enterPhone()
    id = round(time.time())
    data = f"{id}:{email}:{Password}:{FirstName}:{secondName}:{phone}\n"
    saveData(data)

#check login data
def checkExistans(email,password):
    file = open("usersdata.txt", "r")
    data = file.readlines()
    for i in data:
        d = i.split(":")
        if (d[1] == email and d[2] == password):
            return d[0]
    return Login()

#login
def Login():
    print("---------LOGIN------------")
    email=input("EMAIL : ")
    password=input("Password: ")
    user_id=checkExistans(email,password)
    mainPage(user_id)


def entryPage():
    print("""============ Crowd-Funding Entry Page =========== 
    1) Registration
    2) Login """)
    choice = entryInputValidation()
    if (choice == 1):
        Registration()
    elif (choice == 2):
        Login()
