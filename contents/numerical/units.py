import common
def dimensional_calculator():
  print("\nNote: This calculator gives dimensions, but the format might appear non-standard. For example, the area dimension may appear as [L²] but it will be represented as [LL]. You'll need to interpret these results accordingly.\n")
  while True:
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
    if common.quitter()==True:
      break

def units():
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
units()