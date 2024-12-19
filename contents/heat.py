from colorama import Fore
import contents.common as common
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def thermo():
    print("1) Heat and Thermodynamics")
    print("2) Thermal Expansion")
    print("3) Quantity of Heat")
    print("4) Rate of Heat Flow")
    print("5) Ideal Gas")
    while True:
        try: 
            mechno=int(input("Please choose a number of a chapters to go further deep!: "))
            if mechno==1:
                common.call('heatnthermo/heatandtemp','temperature')
            if mechno==2:
                common.call('heatnthermo/thermalexp','thermal')
            if mechno==3:
                common.call('heatnthermo/quantityofheat','quantity')
            if mechno==4:
                common.call('heatnthermo/rateofheatflow','rateofheat')
            if mechno==5:
                common.call('heatnthermo/ideal','ideal')
        except BaseException:
            print("Not an number")
        except:
             print("Out of option or option not open yet!")
        if common.quitter==True:
                break