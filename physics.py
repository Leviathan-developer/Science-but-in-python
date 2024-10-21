def force():
 def m1():
    mass1=int(input("Enter mass of a body: "))  
    print("Analysing the given masses")
    print("Analysing the given distance")
    print("Calculating force...")
    force=(mass1*mass2*0.0000000000667430)/dis
    print("The attraction due to gravity between two bodies =",force)
    print("Where if there is e it means *10^")
 def m2():
  mass2=int(input("Enter mass off a second body"))
  print("Analysing the given masses")
  print("Analysing the given distance")
  print("Calculating force...")
  force=(mass1*mass2*0.0000000000667430)/dis
  print("The attraction due to gravity between two bodies =",force)
  print("Where if there is e it means *10^")
 def distance():
  dis=int(input("Enter distance of a between two bodies (from center): "))
  print("Analysing the given masses")
  print("Analysing the given distance")
  print("Calculating force...")
  force=(mass1*mass2*0.0000000000667430)/dis
  print("The attraction due to gravity between two bodies =",force)
  print("Where if there is e it means *10^")
 mass1=int(input("Enter mass of a body: "))
 mass2=int(input("Enter mass of a second body: "))
 dis=int(input("Enter distance of a between two bodies (from center): "))
 print("Are you sure the given info is correct!")
 response=input("Please type m1(Mass 1), m2(Mass 2), d(Distance) to change or y if its correct: ")
 if response.upper()=="Y":
  print("Analysing the given masses...")
  print("Analysing the given distance...")
  print("Calculating force...")
  force=(mass1*mass2*0.0000000000667430)/dis
  print("The attraction due to gravity between two bodies =",force)
  print("Where if there is e it means *10^")
 elif response.upper()=="M1":
  m1()
 elif response.upper()=="M2":
  m2()
 elif response.upper()=="D":
  distance()
def contents():
 print("***Mechanics***")
 print("***Heat and thermodynamics***")
 print("***Waves and optics***")
 print("***Electricity and Magnetism***")
 print("***Morden physics***")
 unit=input("Please type chapter name")
 n=unit.upper()
 if n=="MECHANICS":
  print("1) Units and Measurment")
  print("2) Vectors and Scalars")
  print("3) Kinematics")
  print("4) Dynamics")
  print("5) Work,Energy and Power")
  print("6) Circular motion")
  print("7) Gravity and Gravitation")
  print("8) Elasticity")
  
#def pendilum():
#def game():
print("Do you want to do physics homework or play game")
master=input("Type Physics/game and hit ENTER")
if master.upper()=="PHYSICS":
 content()
elif master.upper()=="GAMES":
 game()
elif master.upper()=="PHYSICS/GAME":
 print("WTF i ment type Physics or Game only one fool seems like you are not braniny guy to do physis go play game")
 game()
