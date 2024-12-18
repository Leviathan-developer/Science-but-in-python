from colorama import Fore
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def thermo():
    print("1) Heat and Thermodynamics")
    print("2) Thermal Expansion")
    print("3) Quantity of Heat")
    print("4) Rate of Heat Flow")
    print("5) Ideal Gas")
    mechno=int(input("Please choose a number of a chapters to go further deep!: "))
    if mechno==1:
        print("For devs please enter content on no 1")
    elif mechno ==2:
        print("For dev please fill content of no 2")
    elif mechno==3:
        print("For dev please fill content of no 3")
    elif mechno==4:
        print("For dev please fill content of no 4")
    elif mechno==5:
        print("For dev please fill content of no 5")
    else:
        print("Print please choose correct number")
