from colorama import Fore
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def md():
  print("1) Nuclear Physics")
  print("2) Solid and Semiconductor Devices")
  print("3) Recent Trends in Physics")
  mechno=int(input("Please choose a number of a chapters to go further deep!: "))
  if mechno==1:
    print("For devs please enter content on no 1")
  elif mechno ==2:
    print("For dev please fill content of no 2")
  elif mechno==3:
    print("For dev please fill content of no 3")
  else:
    print("Print please choose correct number")
