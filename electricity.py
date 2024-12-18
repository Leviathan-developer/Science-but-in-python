from colorama import Fore
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def elec():
  print("1) Electric Charges")
  print("2) Electric Feild")
  print("3) Electric Potential")
  print("4) Capacitors and Capacitance")
  print("5) Direct Current Circuit")
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
