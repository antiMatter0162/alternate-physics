
def set_initial_parameters(model_to_use):
    """
    Set initial parameters for the simulation.
    """
    n = input("Enter the number of iterations: ")

    try:
        n == int(n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        n = int(input("Enter the number of iterations: "))
    
    n = abs(int(n))
    
    if model_to_use == "2":
        n = int(n) * 100
    elif model_to_use != "1":
        n = int(n) * 10
    # Standardizes time interval

    set_params = input("Do you want to set the parameters? (y/n): ")

    while set_params.lower() not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        set_params = input("Do you want to set the parameters? (y/n): ")
    

    if set_params.lower() == 'y' and model_to_use == "1":
        # Get user input for parameters
        v_0 = input("Enter the initial velocity: ")
        try:
            v_0 == float(v_0)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            v_0 = float(input("Enter the initial velocity: "))
        a = input("Enter the acceleration: ")
        try:
            a == float(a)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            a = float(input("Enter the acceleration: "))
        v_t = input("Enter the velocity threshold: ")
        try:
            v_t == float(v_t)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            v_t = float(input("Enter the velocity threshold: "))
        mass = input("Enter the mass: ")
        try:
            mass == float(mass)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            mass = float(input("Enter the mass: "))
        while float(mass) <= 0.0:
            print("Mass must be greater than 0.0.")
            mass = input("Enter the mass: ")
            try:
                mass == float(mass)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                mass = float(input("Enter the mass: "))
    elif set_params.lower() == 'y' and model_to_use == "2":
        v_0 = input("Enter the initial velocity: ")
        try:
            v_0 == float(v_0)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            v_0 = float(input("Enter the initial velocity: "))
        if float(v_0) >= 50.0:
            print("Initial velocity is above max, setting to 25.0.")
            v_0 = 25.0
        a = input("Enter the acceleration: ")
        try:
            a == float(a)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            a = float(input("Enter the acceleration: "))
        mass = input("Enter the mass: ")
        try:
            mass == float(mass)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            mass = float(input("Enter the mass: "))
        while float(mass) <= 0.0:
            print("Mass must be greater than 0.0.")
            mass = input("Enter the mass: ")
            try:
                mass == float(mass)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                mass = float(input("Enter the mass: "))
        v_t = 0.0
    elif set_params.lower() == 'y':  
        # Get user input for parameters
        v_0 = input("Enter the initial velocity: ")
        try:
            v_0 == float(v_0)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            v_0 = float(input("Enter the initial velocity: "))
        a = input("Enter the acceleration: ")
        try:
            a == float(a)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            a = float(input("Enter the acceleration: "))
        mass = input("Enter the mass: ")
        try:
            mass == float(mass)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            mass = float(input("Enter the mass: "))
        while float(mass) <= 0.0:
            print("Mass must be greater than 0.0.")
            mass = input("Enter the mass: ")
            try:
                mass == float(mass)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                mass = float(input("Enter the mass: "))
        v_t = 0.0
        # Not used in these models, but included so code works
    elif set_params.lower() == 'n':
        print("Using default parameters.")
        # Default parameters
        v_0 = 2.5
        a = 1.5
        v_t = 2.6
        mass = 1.0
    # Set initial parameters
    initial_parameters = {
        "number_of_steps": int(n),
        "initial_conditions": {
            "position": 0.0,
            "velocity": float(v_0),
            "velocity_threshold": float(v_t),
            "acceleration": float(a)

        },
        "simulation_parameters": {
            "mass": float(mass)
        }
    }
    return initial_parameters
