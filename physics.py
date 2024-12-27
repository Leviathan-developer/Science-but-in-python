import contents.mechanics as mechanics
import contents.heat as heat
import contents.electricity as electricity
import contents.morden as morden
import contents.optics as optics
import contents.game as game
import contents.banner as banner
import contents.game as game
import contents.common as common
from colorama import Fore
import time

G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED
def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def contents():
  print("***Mechanics***")
  print("***Heat and thermodynamics***")
  print("***Waves and optics***")
  print("***Electricity and Magnetism***")
  print("***Morden physics***")
  unit=input("Please type chapter name: ")
  n=unit.upper()
  if n.startswith("ME"):
    mechanics.mech()
  if n.startswith("W") or n.startswith("O"):
    optics.wave()
  if n.startswith("E"):
    electricity.elec()
  if n.startswith("MO"):
    morden.md()
  if n.startswith("H"):
    heat.thermo()
  else:
    print("Invalid option!")
banner.anibanner()
print(G+"Do you want to do physics homework or play game for a while?")
while True:
  master=input("Type Physics/game/exit and hit ENTER: ")
  master=master.upper()
  if master.startswith("PH"):
    while True:
      try:
        contents()
        if common.quitter()==True:
          break
      except Exception as e:
        print(f"Error occured in process: {e}")
        if common.quitter()==True:
          break
        time.sleep(1)
    break
  elif master.startswith("GA"):
    game.main()
  elif master.upper()=="PHYSICS/GAME/EXIT":
    print("Please type only one Physic or game!")
  elif master.upper()=="EXIT":
    print("*Exited*")
    break
  else:
    print("Wrong spealling or out of option!!!")
    continue
  time.sleep(1)