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
def dimensional_calculator():
            print("\nNote: This calculator gives dimensions, but the format might appear non-standard. For example, the area dimension may appear as [L²] but it will be represented as [LL]. You'll need to interpret these results accordingly.\n")
            positivelength = "L"
            positivemass = "M"
            positivetime = "T"
            positivekelvin = "K"
            positiveampere = "A"
            positivecandela = "Cd"
            positivemole = "mol"
            negativelength = "L⁻¹"
            negativemass = "M⁻¹"
            negativetime = "T⁻¹"
            negativekelvin = "K⁻¹"
            negativeampere = "A⁻¹"
            acceleration = positivelength + negativetime + negativetime
            force = positivemass + acceleration
            area = positivelength + positivelength
            pressure = force + negativelength + negativelength
            velocity = positivelength + negativetime
            momentum = positivemass + positivelength + negativetime
            impulse = momentum
            energy = force + positivelength
            work = energy
            power = energy + negativetime
            stress = pressure
            angular_velocity = negativetime
            angular_acceleration = negativetime + negativetime
            frequency = negativetime
            moment_of_inertia = positivemass + positivelength + positivelength
            surface_tension = force + negativelength
            coefficient_of_viscosity = positivemass + negativetime + negativelength
            specific_heat = energy + negativemass + negativekelvin
            latent_heat = energy + negativemass
            resistance = positivemass + positivelength + negativetime + negativetime + negativeampere + negativeampere
            permittivity = negativeampere + negativeampere + positivelength + positivetime + positivetime
            permeability = positivemass + positivelength + negativetime + negativetime + negativeampere + negativeampere 
            print("Please type the name of the quantity whose dimension you want to know:")
            print("Available quantities:")
            print("Acceleration, Force, Area, Work, Pressure, Velocity, Momentum, Impulse, Energy, Power, Stress, Angular Velocity, Angular Acceleration, Frequency, Moment of Inertia, Surface Tension, Coefficient of Viscosity, Specific Heat, Latent Heat, Resistance, Permittivity, Permeability")
            choco = input("Enter the name of the quantity you are looking for: ")
            ultrachoco = choco.upper()
            dimensions_dict = {
                "ACCELERATION": acceleration,
                "FORCE": force,
                "AREA": area,
                "PRESSURE": pressure,
                "VELOCITY": velocity,
                "MOMENTUM": momentum,
                "IMPULSE": impulse,
                "ENERGY": energy,
                "WORK": work,
                "POWER": power,
                "STRESS": stress,
                "ANGULAR VELOCITY": angular_velocity,
                "ANGULAR ACCELERATION": angular_acceleration,
                "FREQUENCY": frequency,
                "MOMENT OF INERTIA": moment_of_inertia,
                "SURFACE TENSION": surface_tension,
                "COEFFICIENT OF VISCOSITY": coefficient_of_viscosity,
                "SPECIFIC HEAT": specific_heat,
                "LATENT HEAT": latent_heat,
                "RESISTANCE": resistance,
                "PERMITTIVITY": permittivity,
                "PERMEABILITY": permeability,
            }
            if ultrachoco in dimensions_dict:
                print(f"{choco.title()}: {dimensions_dict[ultrachoco]}")
            else:
                print("Invalid choice. Please check spelling or check if the calculator can process this quantity.")
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
      dimensional_calculator() 
     else:
      print("Print please choose correct number")
    elif norn.upper()=="NOTE":
      print("*****************************************************Definations**********************************************")
      print("<<MEASURMENT>>")
      print("The process of comparing unknown physical quantity with known fixed quantity is called measurment")
      print("<<PHYSICAL QUANTITIE>>")
      print("Def of physical quantity")
      print("<<DIMENSIONALESS VARIABLE>>")
      print("The physical quantity which no dimension but are variables with condition are known as dimensionless variable")
      print("<<DIMENSONLESS CONSTANT>>")
      print("The physical quantities which nither have dimension nor variables are known as dimensionless constant")
      print("<<DIMENSIONAL VARIABLE>>")
      print("The quntity which have dimension and are variable with condition are known as dimensional variable")
      print("<<DIMENSIONAL CONSTANT>>")
      print("The physical quantities which have dimension ansd are constant are known as dimensional constant")
 if n=="WAVES AND OPTICS":
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
  if n=="MORDEN PHYSICS":
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
