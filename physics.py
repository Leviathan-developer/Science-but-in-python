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
 unit=input("Please type chapter name: ")
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
  mechno=int(input("Please choose a number of a chapters to go further deep!: "))
  if mechno==1:
   norn=input("Do you want to go with numerical calculator (Nc) or lesson summary (note) ? ")
   if norn.upper()=="NC":
    print("******************************************************WELCOME TO NUMERICAL CALCULATOR**************************************************")
    print("-----------------------------------------------------================Menu==============-----------------------------------------------")
    print("1) Dimensional calculator")
    numchoice=int(input("Please type a number that corresponds to your need: "))
    if numchoice==1:
     print("Please note the following i made this calculator to give you answer but answer might be in form of some weaird looking dimension for example dimension of area is [L²] but calculator will give in form [MM]you have to multipley M*M yourself and Think its M²,Thankyou!")
     positivelength="L"
     positivemass="M"
     positivetime="T"
     negativelength="L⁻¹"
     negativemass="M⁻¹"
     negativetime="T⁻¹"
     acceleration=positivelength+negativetime+negativetime
     force=positivemass+acceleration
     area=positivelength+positivelength
     pressure=force+negativelength+negativelength
     velocity=positivelength+negativetime
     linearmomentium=positivemass+positivelength+negativetime
     impulse=positivemass+positivelength+negativetime
  elif mechno ==2:
   print("For dev please fill content of no 2")
  elif mechno==3:
   print("For dev please fill content of no 3")
  elif mechno==4:
   print("For dev please fill content of no 4")
  elif mechno==5:
   print("For dev please fill content of no 5")
  elif mechno==6:
   print("For dev please fill content of no 6")
  elif mechno==7:
   print("For dev please fill content of no 7")
  elif mechno==8:
   print("For dev please fill content of no 8")
 else:
    print("Print please choose correct number")
 if n=="HEAT AND THERMODYNAMICS":
  print("1) Heat and temperature")
  print("2) Thermal expansion")
  print("3) Quantity of heat")
  print("4) Rate of heat flow")
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
 if n=="WAVE AND OPTICS":
  print("1) Reflection at curved mirror")
  print("2) Refraction at plane surfaces")
  print("3) Refraction through prisms")
  print("4) Lenes")
  print("5) Dispersion")
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
 if n=="Electricity and Magnetism":
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
 if n=="MORDEN PHYSICS" or "MORDEN PHYSIC":
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
#def game():
print("Do you want to do physics homework or play game")
master=input("Type Physics/game and hit ENTER: ")
if master.upper()=="PHYSICS" or master.upper=="PHYSIC":
 contents()
elif master.upper()=="GAMES" or master.upper=="GAME":
 game()
elif master.upper()=="PHYSICS/GAME":
 print("Please type only one Physic or game!")
elif master.upper()=="EXIT":
 print("*Exited*")
else:
 print("Wrong spealling or out of option!!!")
