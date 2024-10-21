def login():
    username=input("Enter a username: ")
    password=input("Enter a password: ")
    if username == "admin" and password == "admin123":
     print("Welcome buddy")
    elif username=="shapeshifter" and password =="shapeshifterdon'tneedpassword":
     print("*alarms whole system of shapeshifter*")
    else:
     print("No username or password found")
     print("Do you want to create one? ")
    response=input("Please type Y/n: ")
    if response.upper()=="Y":
        signup()


def signup():
    print("***Welcome to sign up***")
    preusername=input("Please set your username: ")
    prepass=input("Please set yourself a password: ")
    print("You are all set !")
    print("Do you want to login?")
    response2=input("Please type Y/n: ")
    if response2.upper()=="Y":
     login()



def main():
 print("***Welcome to our page***")
info=input("Please choose you want to login or sign up: ")
if info.upper()=="LOGIN":
 login()
elif info.upper()=="SIGN UP":
  signup()
else:
    print("Please type Login or Sign up sir") 
    main()