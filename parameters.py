
def set_initial_parameters():
    """
    Set initial parameters for the simulation.
    """
    n = input("Enter the number of steps: ")
    try:
        n == int(n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        n = int(input("Enter the number of steps: "))
    # Ensure n is an integer
    initial_parameters = {
        "number_of_steps": int(n),
        "initial_conditions": {
            "position": 0.0,
            "velocity": 2.5,
            "velocity_threshold": 8.0,
            "acceleration": 1.5

        },
        "simulation_parameters": {
            "gravity": 9.81,
            "mass": 1.0
        }
    }
    return initial_parameters
