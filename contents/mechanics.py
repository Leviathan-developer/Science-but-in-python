from colorama import Fore
import contents.common as common
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED


def mech():
    print("1) Units and Measurment")
    print("2) Vectors and Scalars")
    print("3) Kinematics")
    print("4) Dynamics")
    print("5) Work,Energy and Power")
    print("6) Circular motion")
    print("7) Gravity and Gravitation")
    print("8) Elasticity")
    while True:
        try: 
            mechno=int(input("Please choose a number of a chapters to go further deep!: "))
            if mechno==1:
                common.call('mechanicsnotes/unit_and_measurement','units')
            if mechno==2:
                common.call('mechanicsnotes/vector','vector')
            if mechno==3:
                common.call('mechanicsnotes/kinematics','kinematics')
            if mechno==4:
                common.call('mechanicsnotes/dynamics','dynamics')
            if mechno==5:
                common.call('mechanicsnotes/work','work')
            if mechno==6:
                common.call('mechanicsnotes/circular','circular')
            if mechno==7:
                common.call('mechanicsnotes/gravity','gravity')
            if mechno==8:
                common.call('mechanicsnotes/elasticity','elasticity')
        except BaseException:
            print("Not an number")
        except:
             print("Out of option or option not open yet!")
        if common.quitter==True:
                break