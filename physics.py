import mechanics
import heat
import electricity
import morden
import optics
import game

from colorama import Fore

G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED
def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True

def force():
  while True:
    mass1=int(input("Enter mass of a body: "))
    mass2=int(input("Enter mass of a second body: "))
    dis=int(input("Enter distance of a between two bodies (from center): "))
    force=(mass1*mass2*0.0000000000667430)/dis
    print("The attraction due to gravity between two bodies =",force)
    print("Where if there is e it means *10^")
    if quitter()==True:
      break
 
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
    
print(G+"Do you want to do physics homework or play game")
master=input("Type Physics/game and hit ENTER: ")
if master.upper()=="PHYSICS" or master.upper=="PHYSIC":
 contents()
elif master.upper()=="GAMES" or master.upper=="GAME":
 game.gm()
elif master.upper()=="PHYSICS/GAME":
 print("Please type only one Physic or game!")
elif master.upper()=="EXIT":
 print("*Exited*")
else:
 print("Wrong spealling or out of option!!!")