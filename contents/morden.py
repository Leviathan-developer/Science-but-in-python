from colorama import Fore
import contents.common as common
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def md():
  print("1) Nuclear Physics")
  print("2) Solid and Semiconductor Devices")
  print("3) Recent Trends in Physics")
  while True:
    try: 
        mechno=int(input("Please choose a number of a chapters to go further deep!: "))
        if mechno==1:
            common.call('mordenphysics/nuclearphysics','nuclearphysics')
        if mechno==2:
            common.call('mordenphysics/recenttrends','recenttrends')
        if mechno==3:
            common.call('mordenphysics/solidandsemiconductor','semiconductor')
    except BaseException:
        print("Not an number")
    except:
        print("Out of option or option not open yet!")
    if common.quitter==True:
            break