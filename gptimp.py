def dimensional_calculator():
    print("******************************************************WELCOME TO NUMERICAL CALCULATOR**************************************************")
    print("-----------------------------------------------------================Menu==============-----------------------------------------------")
    print("1) Dimensional calculator")
    
    try:
        numchoice = int(input("Please type a number that corresponds to your need: "))
        
        if numchoice == 1:
            print("\nNote: This calculator gives dimensions, but the format might appear non-standard. For example, the area dimension may appear as [L²] but it will be represented as [LL]. You'll need to interpret these results accordingly.\n")

            # Defining basic units
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

            # Derived units
            acceleration = positivelength + negativetime + negativetime  # L / T²
            force = positivemass + acceleration  # M * L / T²
            area = positivelength + positivelength  # L²
            pressure = force + negativelength + negativelength  # M / T²
            velocity = positivelength + negativetime  # L / T
            momentum = positivemass + positivelength + negativetime  # M * L / T
            impulse = momentum  # Same as momentum
            energy = force + positivelength  # M * L² / T²
            work = energy  # Same as energy
            power = energy + negativetime  # M * L² / T³
            stress = pressure  # Same dimension as pressure M / L / T²
            angular_velocity = negativetime  # 1 / T
            angular_acceleration = negativetime + negativetime  # 1 / T²
            frequency = negativetime  # 1 / T
            moment_of_inertia = positivemass + positivelength + positivelength  # M * L²
            surface_tension = force + negativelength  # M / T²
            coefficient_of_viscosity = positivemass + negativetime + negativelength  # M / L / T
            specific_heat = energy + negativemass + negativekelvin  # L² / T² / K
            latent_heat = energy + negativemass  # L² / T²
            resistance = positivemass + positivelength + negativetime + negativetime + negativeampere + negativeampere  # M * L / T³ / A²
            permittivity = negativeampere + negativeampere + positivelength + positivetime + positivetime  # L³ * T⁴ / A²
            permeability = positivemass + positivelength + negativetime + negativetime + negativeampere + negativeampere  # M * L / T² / A²

            # Prompt user for quantity
            print("Please type the name of the quantity whose dimension you want to know:")
            print("Available quantities:")
            print("Acceleration, Force, Area, Work, Pressure, Velocity, Momentum, Impulse, Energy, Power, Stress, Angular Velocity, Angular Acceleration, Frequency, Moment of Inertia, Surface Tension, Coefficient of Viscosity, Specific Heat, Latent Heat, Resistance, Permittivity, Permeability")
            
            choco = input("Enter the name of the quantity you are looking for: ")
            ultrachoco = choco.upper()
            
            # Dictionary to map user input to dimensions
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
            
            # Output the dimension or error message
            if ultrachoco in dimensions_dict:
                print(f"{choco.title()}: {dimensions_dict[ultrachoco]}")
            else:
                print("Invalid choice. Please check spelling or check if the calculator can process this quantity.")
        else:
            print("Invalid choice. Please enter a valid number.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

# Run the dimensional calculator function
dimensional_calculator()
