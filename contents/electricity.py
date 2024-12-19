from colorama import Fore
import contents.common as common
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def elec():
  print("1) Electric Charges")
  print("2) Electric Feild")
  print("3) Electric Potential")
  print("4) Capacitors and Capacitance")
  print("5) Direct Current Circuit")
  while True:
    try: 
        mechno=int(input("Please choose a number of a chapters to go further deep!: "))
        if mechno==1:
            common.call('electricity/electriccharge','electriccharge')
        if mechno==2:
            common.call('electricity/electricfeild','electricfeild')
        if mechno==3:
            common.call('electricity/electricpotential','electricpotential')
        if mechno==4:
            common.call('electricity/capacitor','capacitor')
        if mechno==5:
            common.call('electricity/directcurrent','directcurrent')
    except BaseException:
        print("Not an number")
    except:
        print("Out of option or option not open yet!")
    if common.quitter==True:
              break